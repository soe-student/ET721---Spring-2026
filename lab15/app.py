"""
Soe Kaythi
Lab 15
"""

import sqlite3
from flask import Flask, render_template, request, jsonify

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="templates",      # because style.css is inside templates
    static_url_path="/static"
)

DATABASE = "item.db"

FULL_NAME = "Soe Kaythi"


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS deleted_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()


@app.route("/")
def home():
    return render_template("index.html", full_name=FULL_NAME)


@app.route("/create_item", methods=["POST"])
def create_item():
    try:
        data = request.get_json()
        name = data.get("name")
        price = data.get("price")

        if not name or price is None:
            return jsonify({"message": "Invalid input"}), 400

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO items (name, price) VALUES (?, ?)",
            (name, price)
        )
        conn.commit()
        conn.close()

        return jsonify({"message": "Item created successfully"}), 201

    except Exception:
        return render_template("error.html", full_name=FULL_NAME), 500


@app.route("/items", methods=["GET"])
def get_items():
    try:
        conn = get_db_connection()
        items = conn.execute("SELECT * FROM items").fetchall()
        conn.close()

        item_list = []
        for item in items:
            item_list.append({
                "id": item["id"],
                "name": item["name"],
                "price": item["price"]
            })

        return jsonify(item_list), 200

    except Exception:
        return render_template("error.html", full_name=FULL_NAME), 500


@app.route("/update_item")
def update_item():
    try:
        item_id = request.args.get("id")
        new_name = request.args.get("name")
        new_price = request.args.get("price")

        conn = get_db_connection()
        conn.execute(
            "UPDATE items SET name = ?, price = ? WHERE id = ?",
            (new_name, new_price, item_id)
        )
        conn.commit()

        updated_item = conn.execute(
            "SELECT * FROM items WHERE id = ?",
            (item_id,)
        ).fetchone()
        conn.close()

        return render_template(
            "update.html",
            item=updated_item,
            full_name=FULL_NAME
        )

    except Exception:
        return render_template("error.html", full_name=FULL_NAME), 500


@app.route("/delete_item")
def delete_item():
    try:
        item_id = request.args.get("id")

        conn = get_db_connection()

        item = conn.execute(
            "SELECT * FROM items WHERE id = ?",
            (item_id,)
        ).fetchone()

        if item is None:
            conn.close()
            return render_template("error.html", full_name=FULL_NAME, message="Item not found."), 404

        conn.execute(
            "INSERT INTO deleted_items (name, price) VALUES (?, ?)",
            (item["name"], item["price"])
        )

        conn.execute(
            "DELETE FROM items WHERE id = ?",
            (item_id,)
        )

        conn.commit()

        deleted_items = conn.execute(
            "SELECT * FROM deleted_items ORDER BY id DESC"
        ).fetchall()

        conn.close()

        return render_template(
            "delete.html",
            item=item,
            deleted_items=deleted_items,
            full_name=FULL_NAME
        )

    except Exception:
        return render_template("error.html", full_name=FULL_NAME), 500
    

    
if __name__ == "__main__":
    init_db()
    app.run(debug=True)