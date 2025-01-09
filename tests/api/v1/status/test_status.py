import httpx

def test_status():
    response = httpx.get("http://localhost:8000/api/v1/status")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}