import pytest
import requests
from datetime import datetime, timedelta, timezone


BASE_URL = "https://reqres.in/api"

def test_Single_user_not_found():
    response=requests.get(f"{BASE_URL}/users/{999}", verify=False)
    assert response.status_code==404
    assert response.reason=="Not Found"
    #pprint.pprint(response.reason)

def test_login_successful():
    user={"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response=requests.post(f"{BASE_URL}/login",json=user, verify=False)
    assert response.status_code == 200
    assert "token" in response.json()

def test_register_unsuccessful():
    data = {"email": "sydney@fife"}
    response=requests.post(f"{BASE_URL}/register",json=data, verify=False)
    assert response.status_code==400
    assert "error" in response.json()
    assert response.json()['error']=="Missing password"

def test_delete_user():
    response=requests.delete(f"{BASE_URL}/users/{2}", verify=False)
    assert response.status_code==204

def test_update_user():
    test_start_time = datetime.now(timezone.utc)
    print(test_start_time)
    data = {"name": "morpheus", "job": "zion resident"}
    response=requests.put(f"{BASE_URL}/users/2",json=data, verify=False)
    assert response.status_code==200
    updated_at = datetime.fromisoformat(response.json()['updatedAt'].replace('Z', '+00:00'))
    assert response.json()['updatedAt']
    # בדיקה האם העדכון בוצע בהפרש של עד 5 שניות מזמן הרצת הטסט
    assert abs(updated_at - test_start_time) < timedelta(seconds=5)
# def test_get_user_by_id_2(base_url):
#     response=requests.get(f"{base_url}/2",verify=False)
#     assert response.status_code==200
#     assert_that(response.json()).contains_key('id')
#     assert_that(response.json()).contains_key('username')
#     assert_that(response.json()['address']).contains_key('suite')
#     assert_that(response.json()['company']).contains_key('name')

#
# params = [(3, "Clementine Bauch"), (4, "Patricia Lebsack"), (5, "Chelsey Dietrich")]
# @pytest.mark.parametrize("user_id, user_name", params)
# def test_get_users(user_id, user_name,base_url):
#     response = requests.get(f"{base_url}/{user_id}",verify=False)
#     assert response.status_code == 200
#     assert response.json()["id"] == user_id
#     assert response.json()["name"] == user_name