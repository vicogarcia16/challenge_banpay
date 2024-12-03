def test_get_ghibli_data_by_username_admin(client, user_data, role_data):
    username = user_data["username"]
    response = client.get(f"/ghibli/{username}/")
    
    assert response.status_code == 200
    response_data = response.json()

    for sub_role in role_data:
        if sub_role != "admin":
            assert sub_role in response_data["admin"]
    
    assert user_data["role"] in response_data
    assert isinstance(response_data["admin"], dict)
    assert len(response_data["admin"]) == len(role_data)-1

def test_get_ghibli_data_by_username_role(client, user_data_no_admin):
    role = user_data_no_admin["role"]
    username = user_data_no_admin["username"]
    response = client.get(f"/ghibli/{username}/")
    
    assert response.status_code == 200
    response_data = response.json()
    assert role in response_data
    assert isinstance(response_data[role], list)
    assert len(response_data) == 1


    