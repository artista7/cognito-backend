"""
Module to populate data using the APIs 

- Create College 
    - Create Drives 
    - Create Students with email, branch, CGPA (right now only these)
        - For each student create a resumes
        - Open resume in Drive 
    - Create Companies 
        - Create Jobs 
        - Open Job Openings
    - Apply in Job Opening

"""
from aws_helpers.cognito import create_new_user, client, confirm_signup
import traceback 
import names
import requests
import random 
# from atnp.models import College, Company
# from users.models import User

API_URL = "http://localhost:8000"

def _confirm_sign_up(name, username, email, phoneNumber, org_type="college"):
    _URL = 'http://localhost:8000/user/signup'
    if org_type=="college":
        data = {
                    "name": name,
                    "username":username,
                    "phoneNumber": phoneNumber,
                    "email": email,
                    "college": {
                            "name": name,
                            "status": "pendingApproval",
                            "primaryContactJson": { 
                                    "name": name,
                                    "username": username,
                                    "phoneNumber": phoneNumber,
                                    "email": email,
                                    "status": "enabled"
                                    },
                            "location":"Gurgaon"}
                }
    else:
        data = {
                    "name": name,
                    "username":username,
                    "phoneNumber": phoneNumber,
                    "email": email,
                    "company": {
                            "name": name,
                            "status": "pendingApproval",
                            "primaryContactJson": { 
                                    "name": name,
                                    "username": username,
                                    "phoneNumber": phoneNumber,
                                    "email": email,
                                    "status": "enabled"
                                    },
                            "location":"Gurgaon"}
                }
    r = requests.post(_URL, json=data)
    return r 

def create_college(name, email, phonenumber):
    try:
        create_new_user(email, name, phonenumber, "college", name)
        confirm_signup("college_{}".format(email), 'password1234')
    except: 
        traceback.print_exc()

def create_company(name, email, phonenumber):
    try:
        create_new_user(email, name, phonenumber, "company", name)
        confirm_signup("company_{}".format(email), 'password1234')
    except:
        traceback.print_exc()

def create_drive(college_id, token, drive_name):
    url = "http://localhost:8000/atnp/drive/"

    payload = {
        "name": drive_name,
        "type": "job",
        "startDate": "2020-01-01T00:00:00.000Z",
        "endDate": "2020-06-01T00:00:00.000Z",
        "status": "active"
        }

    headers = {
    'authorization': "Bearer {}".format(token),
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)
    pass 

def apply_in_drive(drive_id, company_id, token):
    url = "http://localhost:8000/atnp/companyindrive/"

    payload = {"driveId":drive_id,"companyId":company_id,"status":"pendingApproval"}
    headers = {
    'authorization': "Bearer {}".format(token),
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    print(response.json())
    return response.json()

def add_student_in_drive(drive_id, students, token):
    """
    {
                                "studentCollegeId":"2012ME10743",
                                "studentFirstName":"Vivek",
                                "studentLastName":"Verma",
                                "studentMail":"vivekverma239@gmail.com",
                                "studentPhone":"+918750888183"}
    """
    url = "http://localhost:8000/atnp/import_students/"
    payload = { "driveId":drive_id,
                "students":students
                }
    headers = {
    'authorization': "Bearer {}".format(token),
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    return response.json()
    

def create_job(company_id, job_id, token):
    url = "http://localhost:8000/atnp/job/"

    payload = { "title":"Software Engineer {}".format(job_id),
                "description":"Something",
                "positionType":"Full Time",
                "role":"Software Engineer",
                "skills":"Mongo, Django",
                "location":"New Delhi",
                "requirements":"Do well",
                "responsibilities":"Do well",
                "ctcJson":{"ctcMin":1000000,"ctcMax":1100000,"currency":"INR(Indian Rupee)"},
                "companyId":company_id}
    headers = {
        'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNDNiNjU5NzktMWY3ZC00NTFmLWEzYzItNTEzYjg3MDFhZjA3IiwidXNlcm5hbWUiOiJjb21wYW55X2RhdmlkX3NoaXJsZXlAbGVhcm5pbmctc2FnZS5jb20iLCJleHAiOjE1NzY1MTQ1MDQsImVtYWlsIjoiZGF2aWRfc2hpcmxleUBsZWFybmluZy1zYWdlLmNvbSIsIm9yaWdfaWF0IjoxNTc1OTA5NzA0fQ.g_S_rGLDGKjqDQWixMLswC9-_AkRpVhZ1-udrxudkgA",
        }

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.json())

    return response.json()

def create_job_opening(company_in_drive_id, job_id, job_idx, student_in_drive, token):
    url = "http://localhost:8000/atnp/jobopening/"
    payload = {"companyInDriveId":company_in_drive_id,
                "jobId":job_id,
                "title":"Software Engineer {}".format(job_idx),
                "description":"Something",
                "positionType":"Full Time",
                "role":"Software Engineer",
                "skills":"Mongo, Django",
                "location":"New Delhi",
                "requirements":"Do well",
                "responsibilities":"Do well",
                "status":"pendingApproval",
                "ctcJson":"{\"ctcMin\":1000000,\"ctcMax\":1100000,\"currency\":\"INR(Indian Rupee)\"}"
                }

    headers = {
        'authorization': "Bearer {}".format(token),
        }

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.json())
    return response.json()

def create_resume(student_id):
    pass 

def create_resumeopening(student_in_drive, resume, drive):
    pass

def create_application(student_in_drive, job_opening):
    pass 

def _get_pseudo_data():
    name = names.get_full_name()
    email = "{}@learning-sage.com".format(name.lower().replace(" ", "_"))
    return name, email

def _get_student_data(college_id): 
    name = names.get_full_name()
    email = "{}@learning-sage.com".format(name.lower().replace(" ", "_"))
    cgpa = random.gauss(7, 1)
    branch = random.choice(["Chemical Engineering", "Mechanical Engineering", "Compute Science and Engineering",\
                                "Electrical Engineering", "Textile Engineering"])

    data = {
            "studentCollegeId":"2019_ID_{}".format(college_id),
            "studentFirstName":name.split(" ")[0],
            "studentLastName":name.split(" ")[1],
            "studentMail":email,
            "studentPhone":"+918750888183",
            "cgpa": cgpa,
            "branch": branch
        }
    return data

def main():
    # Create college 
    # name, email = _get_pseudo_data()
    # username = "college_{}".format(email)
    # create_college(name, email, "+918750888183")
    # _confirm_sign_up(name, username, email, "+918750888183")
    # Hardcode the API token when running
    college_id = "f004cade-4d0c-47fa-a4f7-1a13d5c46562" 
    college_auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiM2IyODQxODQtNjBlMy00MjdlLTgzN2MtOTIwOGI1MThlMjRjIiwidXNlcm5hbWUiOiJjb2xsZWdlX25hdGFsaWVfYm9zdHdpY2tAbGVhcm5pbmctc2FnZS5jb20iLCJleHAiOjE1NzY1MTQ0MzcsImVtYWlsIjoibmF0YWxpZV9ib3N0d2lja0BsZWFybmluZy1zYWdlLmNvbSIsIm9yaWdfaWF0IjoxNTc1OTA5NjM3fQ.0iHPFEYi5GQre3tzv3a-JWD-WQtWNVExQ2tHUsWf1Sg"

    # Create a drive and print it 
    # drive = create_drive(college_id, college_auth_token, "Placement Drive 2019-2020 - 1")
    drive = {"id":"7ce95aa6-18c5-4b38-a090-dd01e79dc7ed","name":"Placement Drive 2019-2020 - 1","status":"active","type":"job","collegeId":"5a1fd863-b938-480c-b494-973b6eabd517","college":{"id":"5a1fd863-b938-480c-b494-973b6eabd517","name":"Natalie Bostwick","alias":None,"location":"Gurgaon","allowedDomains":None,"status":"pendingApproval","createdAt":"2019-12-08T18:15:14.558823Z","updatedAt":"2019-12-08T18:15:14.558844Z"},"resources":[],"startDate":"2020-01-01T00:00:00Z","endDate":"2020-06-01T00:00:00Z","createdAt":"2019-12-12T17:35:21.673274Z","updatedAt":"2019-12-12T17:35:21.673290Z"}
    students = []
    for idx in range(0, 50):
        students.append(_get_student_data(idx))

    add_student_in_drive(drive.get("id"), students, college_auth_token )

    # name, email = _get_pseudo_data()
    # username = "company_{}".format(email)
    # create_company(name, email, "+918750888183")
    # _confirm_sign_up(name, username, email, "+918750888183", org_type="company")
    # Hardcode the API token when running 

    company_id = "32813eb9-2df7-40f6-af97-324694f25003"
    company_auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNDNiNjU5NzktMWY3ZC00NTFmLWEzYzItNTEzYjg3MDFhZjA3IiwidXNlcm5hbWUiOiJjb21wYW55X2RhdmlkX3NoaXJsZXlAbGVhcm5pbmctc2FnZS5jb20iLCJleHAiOjE1NzY1MTQ1MDQsImVtYWlsIjoiZGF2aWRfc2hpcmxleUBsZWFybmluZy1zYWdlLmNvbSIsIm9yaWdfaWF0IjoxNTc1OTA5NzA0fQ.g_S_rGLDGKjqDQWixMLswC9-_AkRpVhZ1-udrxudkgA"
     

if __name__ == '__main__':
    main()