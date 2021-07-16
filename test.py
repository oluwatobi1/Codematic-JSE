# check for empty string int an query params
# not sent at all

import  requests

BASE = "http://127.0.0.1:5000/great_circle_distance/"
print("Test Cases...")

print("Case 1... Given test case")
response = requests.get(BASE+"?latitude1=55&longitude1=42&latitude2=33&longitude2=89")
print("Response ", response.json())

print("Case 2... No Input Parameters")
response = requests.get(BASE+"")
print("Response ", response.json())

print("Case 3... No Parameters")
response = requests.get(BASE+"?")
print("Response ", response.json())

print("Case 4... Invalid Input type Parameters (str:None)")
response = requests.get(BASE+"?latitude1=55&longitude1=None&latitude2=33&longitude2=89")
print("Response ", response.json())

print("Case 5... Wrong query Parameters (None)")
response = requests.get(BASE+"?latitude=55&longitude1=None&lat=33&longitude2=89")
print("Response ", response.json())

print("Case 6... Empty query Parameters (None)")
response = requests.get(BASE+"?latitude1=55&longitude1=42&latitude2=33&longitude2=")
print("Response ", response.json())

print("Case 7... String query Parameters (None)")
response = requests.get(BASE+"?latitude1=abcd&longitude1=42&latitude2=33&longitude2=")
print("Response ", response.json())