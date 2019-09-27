import requests
from .utils import login
STUDENT_IN_DRIVE_URL = "http://127.0.0.1:8000/atnp/studentindrive/"

def create_sid(student_id, drive_id, headers):
    student_in_drive = {
        	"student_id": student_id,
            "drive_id": drive_id,
            "registrationCode": "984767",
            "studentCollegeId": "ABC34667",
            "studentName": "Test Student",
            "studentMail": "Test Student",
            "studentPhone": "Test Student",
            "status": "pendingApproval",

        }
    r = requests.post(url = STUDENT_IN_DRIVE_URL, json = student_in_drive, headers=headers)
    return r.json()

def get_user(user_id, headers):
    r = requests.get("http://127.0.0.1:8000/atnp/user/", headers=headers)
    return r.json()

def create_sid_with_user(num_users=10, start_idx=2):
    drive_id = None
    college_token = None
    for i in range(num_users):
        idx = 3*i + 2
        if i == 0:
            college_token = login(i)["token"]
            drive_id = "e7f33326-7704-454d-8f7b-baffe7278d01"
            college_headers={'Authorization': 'Bearer {}'.format(college_token)}
        if i == 5:
            college_token = login(3*i)["token"]
            drive_id = "b2c4f6ea-4786-4773-8235-b55d659163e8"
            college_headers={'Authorization': 'Bearer {}'.format(college_token)}
        token = login(idx)["token"]
        headers={'Authorization': 'Bearer {}'.format(token)}
        print(get_user(idx, headers))
        student_id = get_user(idx, headers)['results'][0].get('student_id')
        print(student_id)
        response = create_sid(student_id, drive_id, college_headers)
        print(response)


if __name__ == '__main__':
    # create_sid_with_user()
    create_sid_with_user()
