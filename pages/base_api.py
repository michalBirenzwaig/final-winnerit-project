import requests
import allure

BASE_URL = "https://reqres.in/api"

def get(endpoint):
    with allure.step(f"Performing GET request to {BASE_URL}{endpoint} "):
        """ מבצע בקשת GET ל-API """
        response = requests.get(f"{BASE_URL}{endpoint}", verify=False)
        return response

def post(endpoint, data):
    with allure.step(f"Performing POST request to {BASE_URL}{endpoint} with data: {data}"):
        """ מבצע בקשת POST ל-API """
        response = requests.post(f"{BASE_URL}{endpoint}", json=data, verify=False)
        return response

def put(endpoint, data):
    with allure.step(f"Performing PUT request to {BASE_URL}{endpoint} with data: {data}"):
        """ מבצע בקשת PUT ל-API """
        response = requests.put(f"{BASE_URL}{endpoint}", json=data, verify=False)
        return response

def delete(endpoint):
    with allure.step(f"Performing DELETE request to {BASE_URL}{endpoint}"):
        """ מבצע בקשת DELETE ל-API """
        response = requests.delete(f"{BASE_URL}{endpoint}", verify=False)
        return response