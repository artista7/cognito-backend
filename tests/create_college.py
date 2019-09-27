import requests
from .utils import login
COLLEGE_REGISTRATION_URL = "http://127.0.0.1:8000/atnp/college/"

def create_college(creator, idx, headers):
    college = {
        	      "name": "College{}".format(idx),
        	      "location": "New Delhi",
        	      "phoneNumber": "+011-234563345",
                  "creator_id": creator,
                  "email": "vivekverma239@gmail.com",
                  "phoneNumber": "+91-8750888183",
                  "status": "PENDING"
            }
    r = requests.post(url = COLLEGE_REGISTRATION_URL, json = college, headers=headers)
    print(r)
    return r.json()

def get_user(user_id, headers):
    r = requests.get("http://127.0.0.1:8000/atnp/user/", headers=headers)
    return r.json()

def update_user(user_id, json_data, headers):

    r = requests.patch("http://127.0.0.1:8000/atnp/user/{}/".format(user_id), json=json_data, headers=headers)
    print(r)
    return r.json()

def create_college_and_users(num_users=10, start_idx=0):
    college_id = None
    for i in range(num_users):
        idx = 3*i + start_idx
        token = login(idx)["token"]
        headers={'Authorization': 'Bearer {}'.format(token)}
        user_data = get_user(idx, headers)["results"][0]
        print(user_data)
        if i == 0 :
            response = create_college(idx+1, 0, headers)
            print(response)
            college_id = response.get("id")
        if i == 5 :
            response = create_college(idx+1, 1, headers)
            print(response)
            college_id = response.get("id")
        response = update_user(user_data.get("id"), json_data={"college_id": college_id}, headers=headers)
        print(response)

    # Get the colleges for each user
    for i in range(num_users*3):
        print("Accessing College for user {}".format(i))
        token = login(i)["token"]
        headers={'Authorization': 'Bearer {}'.format(token)}
        response = requests.get(url = COLLEGE_REGISTRATION_URL, headers=headers)
        print(response.json())

if __name__ == '__main__':
    create_college_and_users()
