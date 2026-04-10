from fastapi.testclient import TestClient
from async_service.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "E-Commerce Catalog Service"}


def test_get_products():
    response = client.get("/products")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_product_by_id():
    response = client.get("/products/prod-0001")
    assert response.status_code == 200
    data = response.json()
    assert data["product_id"] == "prod-0001"


def test_get_product_not_found():
    response = client.get("/products/invalid-id")
    assert response.status_code == 404
    assert response.json() == {"detail": "Product not found"}


def test_get_product_batches():
    response = client.get("/products/batch?batch_size=3")
    assert response.status_code == 200
    data = response.json()
    assert data["batch_size"] == 3
    assert len(data["batches"]) > 0


def test_get_recommendations():
    response = client.get("/orders/ORD123/recommendations")
    assert response.status_code == 200
    data = response.json()
    assert data["order_id"] == "ORD123"
    assert len(data["recommendations"]) == 5
    first = data["recommendations"][0]
    assert "product_id" in first
    assert "score" in first
    assert "reason" in first
