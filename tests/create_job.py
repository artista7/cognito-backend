import requests
from .utils import login
JOB_URL = "http://127.0.0.1:8000/atnp/job/"

def create_job(user_id, company_id, headers):
    job = {
        	"title": "Job for Company (User Id {})".format(user_id),
        	"positionType": "Technical",
            "location": "Gurgaon",
        	"role": "Technical",
        	"skills": "MongoDB, Angular",
        	"ctc": "15 LPA",
            "requirements": "Detailed Requirements",
            "responsibilities": "Detailed Responsibilities",
            "criteria": "Detailed Criteria",
            "description": "Blah Blah",
        	"company_id": company_id
        }

    r = requests.post(url = JOB_URL, json = job, headers=headers)
    return r.json()

def get_user(user_id, headers):
    r = requests.get("http://127.0.0.1:8000/atnp/user/", headers=headers)
    # print(r.json())
    return r.json()

def create_job_with_user(user_idx, start_idx=0):
    college_id = None
    idx = user_idx
    token = login(idx)["token"]
    headers={'Authorization': 'Bearer {}'.format(token)}
    company_id = get_user(idx, headers)['results'][0].get('company_id')

    response = create_job(user_idx, company_id, headers)
    print(response)



if __name__ == '__main__':
    create_job_with_user(16)
    create_job_with_user(1)
