import requests
from .utils import login, get_user, get_jobopening
ROUND_URL = "http://127.0.0.1:8000/atnp/round/"

def create_round(company_idx, job_idx, job_opening_id, headers):
    round = {
        	"name": "Job {} Opening Round for Company {}".format(job_idx, company_idx),
        	"jobOpening_id": job_opening_id,
        	"url": "http:/blah.blah",
        	"manager": "Sunil",
            "isInterview": True,
            "startTime": "2019-12-01T14:00:00",
            "endTime": "2019-12-01T16:00:00",
            "deadline": "2019-12-01T16:00:00"
        }

    r = requests.post(url=ROUND_URL, json=round, headers=headers)
    return r.json()

def create_rounds(company_idx, headers):
    # Get Job Openings of the company
    jobOpenings = get_jobopening(headers)["results"]
    for job_idx, jobOpening in enumerate(jobOpenings):
        job_opening_id = jobOpening["id"]
        print(create_round(company_idx, job_idx, job_opening_id, headers))

def main(num_users):
    done_companies = []
    for user_idx in range(num_users):
        college_id = None
        token = login(user_idx)["token"]
        headers={'Authorization': 'Bearer {}'.format(token)}
        user = get_user(user_idx, headers)["results"][0]
        # print(user)
        if user.get('company_id') and user.get('company_id') not in done_companies:
            create_rounds(len(done_companies), headers)
            done_companies.append(user.get('company_id'))


if __name__ == '__main__':
    main(30)
