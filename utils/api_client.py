import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def login(payload):
    # JSONPlaceholder simulates POST — always returns 201
    return requests.post(f"{BASE_URL}/posts", json=payload)

def get_users():
    return requests.get(f"{BASE_URL}/users")