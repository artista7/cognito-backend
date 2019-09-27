import requests
import json

USER_LOGIN_URL = "http://127.0.0.1:8000/api/token/"


def login(id):
    login_profile = {
        "username": "testuser{}".format(id),
        "password": "9415629533testuser{}".format(id)
    }
    r = requests.post(url = USER_LOGIN_URL, json = login_profile)
    return r.json()

def get_user(user_id, headers):
    r = requests.get("http://127.0.0.1:8000/atnp/user/", headers=headers)
    # print(r.json())
    return r.json()

def get_jobs(headers):
    r = requests.get("http://127.0.0.1:8000/atnp/job/", headers=headers)
    print(json.dumps(r.json(), indent=4))
    return r.json()

def get_cids(headers):
    r = requests.get("http://127.0.0.1:8000/atnp/companyindrive/", headers=headers)
    print(json.dumps(r.json(), indent=4))
    return r.json()

def get_drives(headers):
    r = requests.get("http://127.0.0.1:8000/atnp/drive/", headers=headers)
    print(json.dumps(r.json(), indent=4))
    return r.json()

def get_jobopening(headers):
    r = requests.get("http://127.0.0.1:8000/atnp/jobopening/", headers=headers)
    print(json.dumps(r.json(), indent=4))
    return r.json()

def get_rounds(headers):
    r = requests.get("http://127.0.0.1:8000/atnp/round/", headers=headers)
    return r.json()

def get_student_in_drive(headers):
    r = requests.get("http://127.0.0.1:8000/atnp/studentindrive/", headers=headers)
    return r.json()
