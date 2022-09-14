# from django.test import TestCase

# # Create your tests here.


# import requests


# r = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYyOTkzMDQwLCJqdGkiOiI1YzE5ZGE5YjM0ZWI0NWJjYWFjMjI2MjBkNzJjMmNlZiIsInVzZXJfaWQiOjJ9.5Wd3vuc2BGu2SQA8Z4RDNFfQSq5UTliYQK-B7O3mIGo"

# res = requests.post("http://127.0.0.1:8000/logout/", data={
#     "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2MzA3OTE0MCwianRpIjoiMDk4Y2VkZDYyNTEyNDczZWE1N2FlOGUxODM5MWM2NmIiLCJ1c2VyX2lkIjoyfQ.zMGwmxnYrQc0WxJ11uVrJ6mJ538AgUfAYu-HhgSh8kY"
# }, headers={
#     "Authorization": "Bearer {}".format(r) 
# })

# print(res.status_code)
# print(res.json())