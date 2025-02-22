import pytest
import requests
from datetime import datetime, timedelta, timezone
from pages.base_api import get, post, put, delete

# משתמש לא נמצא
@pytest.mark.api
def test_Single_user_not_found():
    # response=requests.get(f"{BASE_URL}/users/{999}", verify=False)
    response = get("/users/999")
    assert response.status_code==404
    assert response.reason=="Not Found"

# שליפת משתמש
@pytest.mark.api
def test_get_user():
    user_id=3
    response = get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["data"]["id"]==user_id
    assert "first_name" in response.json()["data"]
    assert "last_name" in response.json()["data"]

# בדיקת כמות היוזרים
@pytest.mark.api
def test_count_users():
    response = get("/users?delay=3")
    assert len(response.json()["data"]) == 6

# בדיקה שכל היוזרים מכילים id, email, first_name, last_name, avatar
@pytest.mark.api
def test_check_all_params():
    response = get("/users?page=2")
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
@pytest.mark.api
@pytest.mark.parametrize("user_id, expected_name", params)
def test_get_users(user_id, expected_name):
    response = get("/unknown")
    assert response.status_code == 200
    response_data = response.json()
    for item in response_data["data"]:
       if item["id"] == user_id:
            assert item["name"] == expected_name

# התחברות בהצלחה עם טוקן
@pytest.mark.api
def test_login_successful():
    user={"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = post("/login", user)
    assert response.status_code == 200
    assert "token" in response.json()

# משתמש נרשם ללא סיסמא
@pytest.mark.api
def test_register_unsuccessful():
    data = {"email": "sydney@fife"}
    response = post("/register", data)
    assert response.status_code==400
    assert "error" in response.json()
    assert response.json()['error']=="Missing password"

# יצירת משתמש
@pytest.mark.api
def test_create_user():
    data={ "name": "morpheus", "job": "leader" }
    response = post("/users/2", data)
    assert response.status_code==201
    assert "id" in response.json()
    assert "morpheus"==response.json()["name"]
    assert "leader"==response.json()["job"]

# מחיקת משתמש
@pytest.mark.api
def test_delete_user():
    response = delete("/users/2")
    assert response.status_code==204

# עדכון משתמש
@pytest.mark.api
def test_update_user():
    test_start_time = datetime.now(timezone.utc)
    print(test_start_time)
    data = {"name": "morpheus", "job": "zion resident"}
    response = put("/users/2", data)
    assert response.status_code==200
    updated_at = datetime.fromisoformat(response.json()['updatedAt'].replace('Z', '+00:00'))
    assert response.json()['updatedAt']
    # בדיקה האם העדכון בוצע בהפרש של עד 5 שניות מזמן הרצת הטסט
    assert abs(updated_at - test_start_time) < timedelta(seconds=5)







