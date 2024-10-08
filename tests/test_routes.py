from app import create_app
import pytest

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        return client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Home | HTML5" in response.data

def test_about_page(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert b"About Us | HTML5" in response.data

def test_contact_page(client):
    response = client.get('/contact-us')
    assert response.status_code == 200
    assert b"Contact Us" in response.data