import pytest
import requests
from datetime import datetime, timedelta, timezone

BASE_URL = "https://reqres.in/api"

# משתמש לא נמצא
def test_Single_user_not_found():
    response=requests.get(f"{BASE_URL}/users/{999}", verify=False)
    assert response.status_code==404
    assert response.reason=="Not Found"
    #pprint.pprint(response.reason)

# שליפת משתמש
def test_get_user():
    id=3
    response=requests.get(f"{BASE_URL}/users/{id}",verify=False)
    assert response.status_code == 200
    assert response.json()["data"]["id"]==id
    assert "first_name" in response.json()["data"]
    assert "last_name" in response.json()["data"]

# בדיקת כמות היוזרים
def test_count_users():
    response=requests.get(f"{BASE_URL}/users?delay=3",verify=False)
    assert len(response.json()["data"]) == 6

# בדיקה שכל היוזרים מכילים id, email, first_name, last_name, avatar
def test_check_all_params():
    response = requests.get(f"{BASE_URL}/users?page=2", verify=False)
    response_data = response.json()["data"]
    print(response_data)
    assert response.status_code == 200
    for user in response_data:
        assert "id" in user
        assert "email" in user
        assert "first_name" in user
        assert "last_name" in user
        assert "avatar" in user

# pytest.mark.parametrizeטסט שמקבל משתמשים ובודק את תקינות שם המשתמש עם שימוש ב
params = [(1, "cerulean"), (3, "true red"), (5, "tigerlily")]
@pytest.mark.parametrize("user_id, expected_name", params)
def test_get_users(user_id, expected_name):
    response = requests.get(f"{BASE_URL}/unknown", verify=False)
    assert response.status_code == 200
    response_data = response.json()
    for item in response_data["data"]:
       if item["id"] == user_id:
            assert item["name"] == expected_name

# התחברות בהצלחה עם טוקן
def test_login_successful():
    user={"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response=requests.post(f"{BASE_URL}/login",json=user, verify=False)
    assert response.status_code == 200
    assert "token" in response.json()

# משתמש נרשם ללא סיסמא
def test_register_unsuccessful():
    data = {"email": "sydney@fife"}
    response=requests.post(f"{BASE_URL}/register",json=data, verify=False)
    assert response.status_code==400
    assert "error" in response.json()
    assert response.json()['error']=="Missing password"

# יצירת משתמש
def test_create_user():
    data={ "name": "morpheus", "job": "leader" }
    response=requests.post(f"{BASE_URL}/users/{2}",json=data, verify=False)
    assert response.status_code==201
    assert "id" in response.json()
    assert "morpheus"==response.json()["name"]
    assert "leader"==response.json()["job"]

# מחיקת משתמש
def test_delete_user():
    response=requests.delete(f"{BASE_URL}/users/{2}", verify=False)
    assert response.status_code==204

# עדכון משתמש
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

# def test_NIS():
#     data = {"jj"}
#     response=requests.put(f"{BASE_URL}/users/29000",json=data, verify=False)
#     print(response.json())

# def test_get_user_by_id_2(base_url):
#     response=requests.get(f"{base_url}/2",verify=False)
#     assert response.status_code==200
#     assert_that(response.json()).contains_key('id')
#     assert_that(response.json()).contains_key('username')
#     assert_that(response.json()['address']).contains_key('suite')
#     assert_that(response.json()['company']).contains_key('name')

#






