from fastapi import HTTPException
from db.db_user import validate_email_and_username

def test_create_user(client, user_data):
    user_data["username"] = "new_user"
    response = client.post("/user/", json=user_data)
    assert response.status_code == 200 
    assert response.json()["username"] == user_data["username"]
    assert response.json()["email"] == user_data["email"]
    assert response.json()["role"] == user_data["role"]

def test_get_users(client):
    response = client.get("/user/all/")
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]["username"] == "user1"
    assert response.json()[1]["username"] == "user2"

def test_get_user_by_id(client, mock_db_session, user_data):
    response = client.get(f"/user/{user_data['id']}/")
    assert response.status_code == 200
    assert response.json()["username"] == user_data["username"]
    assert response.json()["email"] == user_data["email"]
    assert response.json()["role"] == user_data["role"]

def test_update_user(client, updated_data, user_data, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.put(f"/user/{user_data['id']}/", 
                          json=updated_data, headers=headers)
    assert response.status_code == 200
    assert response.json()["username"] == updated_data["username"]
    assert response.json()["email"] == updated_data["email"]
    assert response.json()["role"] == updated_data["role"]

def test_delete_user(client, user_data, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.delete(f"/user/{user_data['id']}/", headers=headers)
    assert response.status_code == 200
    assert response.json()["message"] == "El usuario ha sido eliminado"

def test_validate_username_already_exists(mock_db_session, existing_user_by_username):
    existing_user_by_username("user1")
    try:
        validate_email_and_username(mock_db_session, email="unique_email@example.com",
                                    username="user1")
    except HTTPException as e:
        assert e.status_code == 400
        assert e.detail == "El username 'user1' ya existe en la base de datos"

def test_validate_email_already_exists(mock_db_session, existing_user_by_email):
    existing_user_by_email("user1@example.com")
    try:
        validate_email_and_username(mock_db_session, email="user1@example.com",
                                    username="user2")
    except HTTPException as e:
        assert e.status_code == 400
        assert e.detail == "El correo electrónico 'user1@example.com' ya está registrado en la base de datos"

def test_validate_exclude_user(mock_db_session, existing_user_with_id):
    existing_user_with_id(1)
    result = validate_email_and_username(mock_db_session, email="user1@example.com", username="user1", exclude_user_id=1)
    assert result is None

def test_validate_unique_data(no_users_found):
    result = validate_email_and_username(no_users_found, email="unique_email@example.com", username="unique_username")
    assert result is None

