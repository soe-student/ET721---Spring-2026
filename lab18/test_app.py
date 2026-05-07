import os
import sqlite3
import pytest
from app import app


#Test Database 

def init_test_db():
    if os.path.exists('test.db'):
        os.remove('test.db')
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@pytest.fixture
def client(monkeypatch):
    def test_get_db():
        conn = sqlite3.connect('test.db')
        conn.row_factory = sqlite3.Row
        return conn
    
    from app import get_db
    monkeypatch.setattr('app.get_db', test_get_db)
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'test_secret'
    
    init_test_db()
    with app.test_client() as client:
        yield client

    if os.path.exists('test.db'):
        os.remove('test.db')

def test_home_redirect(client):
    response = client.get('/')
    assert response.status_code == 302
    assert response.location == 'http://localhost/notes'

def test_login_success(client):
    response = client.post('/login', data={
        'username': 'test_user',
        'password': 'test_password'
    })

    response = client.post('/signup', data={
        'username': 'test_user',
        'email': 'test@example.com',
        'password': 'test_password'
    })

    assert response.status_code == 302
    assert response.location == 'http://localhost/notes'
