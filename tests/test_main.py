from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}

def test_get_suggestions():
    response = client.get("/suggestions?q=London&latitude=43.70011&longitude=-79.4163")
    assert response.status_code == 200
    response_json = response.json()
    assert "suggestions" in response_json
    assert len(response_json["suggestions"]) > 0

def test_get_suggestions_empty_list():
    response = client.get("/suggestions?q=SomeRandomCityInTheMiddleOfNowhere&latitude=0&longitude=0")
    assert response.status_code == 200
    assert response.json() == {"suggestions": []}
