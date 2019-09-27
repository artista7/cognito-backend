import requests
from .utils import login, get_drives
DRIVE_URL = "http://127.0.0.1:8000/atnp/companyindrive/"

def create_cid(company_id, drive_id, headers):
    drive = {
        	"company_id": company_id,
            "drive_id": drive_id,
            "status": "pendingApproval"
        }
    r = requests.post(url = DRIVE_URL, json = drive, headers=headers)
    return r.json()

def get_user(user_id, headers):
    r = requests.get("http://127.0.0.1:8000/atnp/user/", headers=headers)
    return r.json()

def create_cid_with_user(user_idx, start_idx=0):
    college_id = None
    idx = user_idx
    token = login(idx)["token"]
    headers={'Authorization': 'Bearer {}'.format(token)}
    company_id = get_user(idx, headers)['results'][0].get('company_id')
    drives = get_drives(headers)["results"]
    for drive in drives:
        response = create_cid(company_id, drive.get("id"), headers)
    print(response)


if __name__ == '__main__':
    create_cid_with_user(1)
    create_cid_with_user(16)
    # create_drive_with_user(0)
