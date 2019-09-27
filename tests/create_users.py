import requests

USER_REGISTRATION_URL = "http://127.0.0.1:8000/atnp/user/"
user_profile = {
	"user": {
		"username": "shubham-gupta",
		"email": "vivek.verma@learning-sage.com",
		"password": "9415629533"
	},
	"name": "Shubham Gupta",
	"location": "India",
	"phoneNuber": "+918750888183",
	"role": "admin"
}

def create_user(username, name, email="vivekverma239@gmail.com",
                password="9415629533", location="India",
                phoneNumber="+918750888183",
                role="user"):

    user_profile = {
    	"user": {
    		"username": username,
    		"email": email,
    		"password": password+username
    	},
    	"name": name,
    	"location": location,
    	"phoneNuber": phoneNumber,
    	"role": role
    }
    import json
    print(json.dumps(user_profile, indent=4))
    r = requests.post(url = USER_REGISTRATION_URL, json = user_profile)
    print(r.json())


def create_random_users(num=30):
    for i in range(15, num):
        username = "testuser{}".format(i)
        name = "Test User {}".format(i)
        create_user(username, name)

if __name__ == '__main__':
    create_random_users()
