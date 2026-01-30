import requests
import json

time_range = "2m"
latitude_from_user=input(("please input the latitude of your location: "))
longitude_from_user=input(("please input the longitude of your location: "))
latitude_for_spain="40.00000000"
longitude_from_spain="-4.00000000"
latitude_for_germany="51.00000000"
longitude_from_germany="9.00000000"
api_url =f"https://api.open-meteo.com/v1/forecast?latitude={latitude_from_user}&longitude={longitude_from_user}&hourly=temperature_{time_range}"
response = requests.get(api_url)
print(response)

if response.status_code == 200:
    fild_name= f"temperature_{time_range}"
    print("Request successful!")
    data = response.json()
    for temp in data["hourly"][fild_name]:
        print("your location temp in 2 minute intervals " , temp)
else:
    print(f"Request failed with status code: {response.status_code}")
    print(f"Error details: {response.text}")

api_url =f"https://api.open-meteo.com/v1/forecast?latitude={latitude_for_spain}&longitude={longitude_from_spain}&hourly=temperature_{time_range}"
response = requests.get(api_url)
print("spain location", response)
if response.status_code == 200:
    fild_name= f"temperature_{time_range}"
    data = response.json()
    print("spain temp", data["hourly"][fild_name])

else:
    print(f"Request failed with status code: {response.status_code}")
    print(f"Error details: {response.text}")







