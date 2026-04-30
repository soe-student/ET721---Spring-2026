from flask import Flask, request, render_template, redirect, url_for
import os
import time
import sqlite3

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def get_db():
    conn = sqlite3.connect('images.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS images (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            filename  TEXT NOT NULL,
            uploaded_at TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    success = None

    if request.method == 'POST':
        if 'image' not in request.files or request.files['image'].filename == '':
            error = 'Please select an image'
        else:
            file = request.files['image']
            if allowed_file(file.filename):
                name, ext = os.path.splitext(file.filename)
                unique_filename = f"{name}_{int(time.time())}{ext}"
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))

                conn = get_db()
                conn.execute(
                    'INSERT INTO images (filename, uploaded_at) VALUES (?, ?)',
                    (unique_filename, time.strftime('%Y-%m-%d %H:%M:%S'))
                )
                conn.commit()
                conn.close()

                success = 'Image uploaded successfully'
            else:
                error = 'Invalid file type.'

    # Load images from database
    conn = get_db()
    images = conn.execute('SELECT filename, uploaded_at FROM images ORDER BY id DESC').fetchall()
    conn.close()

    return render_template('index.html', error=error, success=success, images=images)


@app.route('/delete/<filename>', methods=['POST'])
def delete(filename):

    filepath = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(filepath):
        os.remove(filepath)

    conn = get_db()
    conn.execute('DELETE FROM images WHERE filename = ?', (filename,))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))


if __name__ == '__main__':
    init_db()   
    app.run(debug=True, port=5001)