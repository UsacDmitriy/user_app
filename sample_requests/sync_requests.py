import requests
import json

response = requests.get('http://127.0.0.1:8000/user/0', headers={})
print(response.json())
print("headers: ", response.headers, type(response.headers))
print(response.json(), type(response.json()))

sample_data = {
    "name": "bob",
    "liked_posts": [
        0,
        0,
        1,
        2,
    ],
    "short_description": "string",
    "long_bio": "string"
}
print("")
json_data = json.dumps(sample_data)
print("json data: ", json_data, type(json_data))
print("original data:", sample_data, type(sample_data))
post_response = requests.post('http://127.0.0.1:8000/user/', headers={}, data=json_data)
print("post request response: ", post_response.json())
post_response = requests.post('http://127.0.0.1:8000/user/', headers={}, json=sample_data)
print("post request response: ", post_response.json())
print("post request response: ", post_response.status_code)
print("post request response: ", post_response.headers)

