"""
Soe Kaythi
March 31, 2026
Rest API Unit Testing
"""

# set-up a reusable component using pytest.fixture
import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True  # enables testing mode
    with app.test_client() as client:
        yield client


# test homepage
def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 200


# test POST request (create item)
def test_create_item(client):
    response = client.post("/create_item", json={'name': 'Book', 'price': 12.99})
    assert response.status_code == 201
    data = response.get_json()
    assert data['message'] == 'Item created successfully'


# test GET all items
def test_get_items(client):
    client.post("/create_item", json={'name': 'Bookbag', 'price': 130})
    response = client.get("/items")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)


# test GET update item
def test_update_item(client):
    client.post("/create_item", json={'name': 'Phone', 'price': 899.99})
    response = client.get("/update_item?id=1&name=Smartphone&price=999.99")
    assert response.status_code == 200


# test GET delete item
def test_delete_item(client):
    client.post("/create_item", json={'name': 'Laptop', 'price': 999.99})
    response = client.get("/delete_item?id=1")
    assert response.status_code == 200