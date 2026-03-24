import requests
import json

locations = [
    ("Germany (Hesse)", 51.00000000, 9.00000000),
    ("Spain (Castilla-La Mancha)", 40.00000000, -4.00000000)
]

def get_weather(latitude, longitude):
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return None

def display_temperatures(data):
    if data is None:
        print("No data available.")
        return

    temperatures = data["hourly"]["temperature_2m"]

    print("\nTemperatures:")
    for temp in temperatures:  # iteration
        if temp is not None:   # selection
            print(temp)

print("Choose a location:")
for i in range(len(locations)):
    print(f"{i+1}: {locations[i][0]}")

while True:
    try:
        choice = int(input("Enter number: "))
        if 1 <= choice <= len(locations):
            break
        else:
            print("Invalid choice. Try again.")
    except:
        print("Please enter a valid number.")

selected_location = locations[choice - 1]
name, lat, lon = selected_location

print(f"\nYou selected: {name}")


weather_data = get_weather(lat, lon)
display_temperatures(weather_data)
