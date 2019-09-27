import requests
from .utils import login
DRIVE_URL = "http://127.0.0.1:8000/atnp/drive/"

def create_drive(college_id, headers):
    drive = {
        	"name": "Drive 2019-2020 College 2",
        	"status": "Yet to start",
        	"location": "New Delhi",
        	"drivetype": "Placement",
        	"description": "This is description",
        	"startDate": "2012-02-21 10:28:45",
        	"endDate": "2012-02-21 10:28:45",
        	# "college_id": "fc5e1587-9fda-465a-8011-0ee7bee5c6b1"
            "college_id": college_id
        }
    r = requests.post(url = DRIVE_URL, json = drive, headers=headers)
    return r.json()

def get_user(user_id, headers):
    r = requests.get("http://127.0.0.1:8000/atnp/user/", headers=headers)
    return r.json()

def create_drive_with_user(user_idx, start_idx=0):
    college_id = None
    idx = user_idx
    token = login(idx)["token"]
    headers={'Authorization': 'Bearer {}'.format(token)}
    college_id = get_user(idx, headers)["results"][0].get("college_id")
    response = create_drive(college_id, headers)
    print(response)



if __name__ == '__main__':
    create_drive_with_user(15)
    # create_drive_with_user(0)
