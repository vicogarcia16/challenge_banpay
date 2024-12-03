import jwt

def test_login_success(client, user_data):
    login_data = {"username": user_data["username"], "password": user_data["password"]}
    response = client.post("/login/", json=login_data)
    assert response.status_code == 200
    response_data = response.json()
    
    assert "access_token" in response_data 
    assert "refresh_token" in response_data
    assert "token_type" in response_data
    assert "access_expires_in" in response_data
    assert "refresh_expires_in" in response_data
    decoded_token = jwt.decode(response_data["access_token"], options={"verify_signature": False})
    assert decoded_token["username"] == user_data["username"]

def test_login_refresh_token(client, user_data):
    login_data = {"username": user_data["username"], "password": user_data["password"]}
    response = client.post("/login/", json=login_data)
    auth_token = response.json()["refresh_token"]
    response = client.post("/refresh/", json={"refresh_token": auth_token})
    assert response.status_code == 200
    response_data = response.json()
    assert "access_token" in response_data
    
def test_login_refresh_token_invalid(client, user_data):
    login_data = {"username": user_data["username"], "password": user_data["password"]}
    response = client.post("/login/", json=login_data)
    invalid_refresh_token = "invalid_refresh_token"
    response = client.post("/refresh/", json={"refresh_token": invalid_refresh_token})
    assert response.status_code == 401
    assert response.json()["detail"] == "Refresh token inválido o expirado"