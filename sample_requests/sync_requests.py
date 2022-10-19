import requests
import json


def get_and_parse_user(base_url: str, endpoint: str, user_id: int):
    full_url = base_url + endpoint + str(user_id)
    response = requests.get(full_url)
    post_response = requests.post(full_url)
    return post_response.json()



















# sample_data = {
#     "name": "bob",
#     "liked_posts": [
#         0,
#         0,
#         1,
#         2,
#     ],
#     "short_description": "string",
#     "long_bio": "string"
# }
#
# json_data = json.dumps(sample_data)
# post_response = requests.post('http://127.0.0.1:8000/user/', headers={}, data=json_data)
# post_response = requests.post('http://127.0.0.1:8000/user/', headers={}, json=sample_data)
