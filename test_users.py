import json
from jsonschema import validate

def test_get_users(client):
    response = client.get("/users?page=2")
    assert response.status_code == 200

    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)
    assert len(data["data"]) > 0

def test_update_user(client):
    payload = {
        "name": "John",
        "job": "Senior QA"
    }
    headers = {"Authorization": "Bearer your_valid_token"}
    response = client.put("/users/2", json=payload, headers=headers)
    assert response.status_code == 200



    data = response.json()
    assert data["name"] == payload["name"]
    assert data["job"] == payload["job"]
    assert "id" in data
    assert "createdAt" in data

def test_user_schema(client):
    response = client.get("/users/2")
    assert response.status_code == 200
    data = response.json()

    with open("data/user_schema.json") as f:
        schema = json.load(f)

    validate(instance=data, schema=schema)

def test_update_user(client):
    payload = {
        "name": "John",
        "job": "Senior QA"
    }
    response = client.put("/users/2", json=payload)  # ✅ Use PUT, not POST
    assert response.status_code == 200  # ✅ 200 OK is correct for update

    data = response.json()
    assert data["job"] == payload["job"]
    assert "updatedAt" in data


def test_response_time(client):
    response = client.get("/users")  # ✅ this becomes https://reqres.in/api/users
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2


def test_get_nonexistent_user(client):
    """Negative test: Get user that doesn't exist"""
    response = client.get("/users/9999")

    # Reqres returns 404 for non-existent users
    assert response.status_code == 404


    if response.status_code == 200:
        data = response.json()
        assert data == {} or "data" not in data
