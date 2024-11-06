from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_search():
    response = client.get("/v1/search?user_id=VALID_USER_ID")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) <= 4
