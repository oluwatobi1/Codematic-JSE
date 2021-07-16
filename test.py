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




#################### logic ##########
print("Case 8... all Zero input")
response = requests.get(BASE+"?latitude1=0&longitude1=0&latitude2=0&longitude2=0")
print("Response ", response.json())


print("Case 8...  small negative input")
response = requests.get(BASE+"?latitude1=-10&longitude1=0.00000000001&latitude2=0.001&longitude2=0.11111")
print("Response ", response.json())

print("Case 9.. Large negative input")
response = requests.get(BASE+"?latitude1=-10&longitude1=100000000000&latitude2=0.001&longitude2=0.11111")
print("Response ", response.json())

print("Case 10.. Latitude outside range of (90 to -90)")
response = requests.get(BASE+"?latitude1=-944&longitude1=10000&latitude2=677&longitude2=10")
print("Response ", response.json())

print("Case 11.. Latitude outside range of (90 to -90)")
response = requests.get(BASE+"?latitude1=-80&longitude1=10000&latitude2=677&longitude2=10")
print("Response ", response.json())


print("Case 12... Longitude outside range (-180 to 180)")
response = requests.get(BASE+"?latitude1=55&longitude1=420&latitude2=33&longitude2=89")
print("Response ", response.json())

print("Case 13... Longitude outside range (-180 to 180)")
response = requests.get(BASE+"?latitude1=55&longitude1=42&latitude2=33&longitude2=809")
print("Response ", response.json())



