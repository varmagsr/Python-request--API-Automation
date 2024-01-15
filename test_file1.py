import requests
import random
import json
import string

#base url:
base_url = "https://gorest.co.in"

#Auth Token:
auth_token = "Bearer ae79b10172657951f222f320b29679f8e67b9e11a7ae04d53fa6e520d5b497c9"

#GET Request:


def get_request():
    url = base_url + "/public/v2/users/5914149"
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    #print("response data", json_str)

#POST Request


def post_request():
    url = base_url + "/public/v2/users/5914149"
    headers = {"Authorization": auth_token}
    data = {
            "name":	"Sam TOM",
            "email": "josh@parker.test",
            "gender": "male",
            "status": "active"
            }
    response = requests.post(url, json=data, headers=headers)
    print("status code:", response.status_code)
    assert response.status_code == 201
    json_data2 = response.json()
    json_str2 = json.dumps(json_data2, indent=4)
    print("response data", json_str2)
    user_id = json_data2["id"]


#PUT Request

def put_request():
    url = base_url + "/public/v2/users/{user_id}"
    headers = {"Authorization": auth_token}
    data = {
            "name":	"Sam wwM",
            "email": "joooo@parker.test",
            "gender": "male",
            "status": "active"
            }
    response = requests.put(url, json=data, headers=headers)
    print("status code:", response.status_code)
    assert response.status_code == 200
    json_data3 = response.json()
    json_str3 = json.dumps(json_data3, indent=4)
    print("response data", json_str3)



#DELETE Request
def delete_request():
    url = base_url + "/public/v2/users/{user_id}"
    headers = {"Authorization": auth_token}
    response = requests.delete(url, headers=headers)
    print("status code:", response.status_code)
    assert response.status_code == 204
   


#Calling request
get_request()
post_request()
put_request(user_id)
delete_request(user_id)
