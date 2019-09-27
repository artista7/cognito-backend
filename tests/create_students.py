import requests
from .utils import login
STUDENT_REGISTRATION_URL = "http://127.0.0.1:8000/atnp/student/"

def create_student(creator, idx, headers):
    student = {
                  "name" : "Student {}".format(creator),
                  "aboutMe" : "Student {}".format(creator),
                  "userName": "Student {}".format(creator),
                  "email": "test@gmail.com",
                  "education" : "Blah Blah School",
                  "credits" : "10",
                  "profilePicS3Path": "Null",
                  "phoneNumber": "+918750888183",
                  "skills": "Skills",
                  "projects": "None",
                  "work": "None"
            }
    print(student)
    r = requests.post(url = STUDENT_REGISTRATION_URL, json = student, headers=headers)
    print(r)
    return r.json()

def get_user(user_id, headers):
    r = requests.get("http://127.0.0.1:8000/atnp/user/", headers=headers)
    return r.json()

def update_user(user_id, json_data, headers):

    r = requests.patch("http://127.0.0.1:8000/atnp/user/{}/".format(user_id), json=json_data, headers=headers)
    print(r)
    return r.json()

def create_and_link_student(num_users=10, start_idx=2):
    student_id = None
    for i in range(num_users):
        idx = 3*i + start_idx
        token = login(idx)["token"]
        headers={'Authorization': 'Bearer {}'.format(token)}
        user_data = get_user(idx, headers)["results"][0]
        print(user_data)
        response = create_student(idx+1, idx, headers)
        print(response)
        student_id = response.get("id")
        response = update_user(user_data.get("id"), json_data={"student_id": student_id}, headers=headers)
        print(response)

    # Get the colleges for each user
    for i in range(num_users*3):
        print("Accessing College for user {}".format(i))
        token = login(i)["token"]
        headers={'Authorization': 'Bearer {}'.format(token)}
        response = requests.get(url = STUDENT_REGISTRATION_URL, headers=headers)
        print(response.json())

if __name__ == '__main__':
    create_and_link_student()
