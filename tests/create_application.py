import requests
from .utils import login, get_user, get_jobopening, get_student_in_drive, get_rounds
APPLICATION_URL = "http://127.0.0.1:8000/atnp/application/"

def create_application(jobOpening_id, currentRound_id, studentInDrive_id, headers):
    application = {
        	"studentInDrive_id": studentInDrive_id,
        	"jobOpening_id": jobOpening_id,
            "currentRound_id": currentRound_id,
            "status": "Pending"
        }

    r = requests.post(url=APPLICATION_URL, json=application, headers=headers)
    return r.json()

def create_applications_for_each_job(student_idx, headers):
    studentInDrive = get_student_in_drive(headers)["results"][0]

    # Get Job Openings of the company
    jobOpenings = get_jobopening(headers)["results"]
    for job_idx, jobOpening in enumerate(jobOpenings):
        # For each job opening get the first rounds
        job_opening_id = jobOpening["id"]
        rounds = get_rounds(headers)["results"]
        valid = [round for round in rounds if round["jobOpening_id"] == jobOpening["id"]]
        if valid:
            print(create_application(job_opening_id, valid[0]["id"], studentInDrive["id"], headers))

def main(num_users):
    done_companies = []
    for user_idx in range(num_users):
        token = login(user_idx)["token"]
        headers={'Authorization': 'Bearer {}'.format(token)}
        user = get_user(user_idx, headers)["results"][0]
        # print(user)
        if user.get('student_id'):
            create_applications_for_each_job(user_idx, headers)


if __name__ == '__main__':
    main(30)
