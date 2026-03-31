import requests

locations = [
    ("Germany (Hesse)", 51.0, 9.0),
    ("Spain (Castilla-La Mancha)", 40.0, -4.0)
]

def get_weather(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return None


def analyze_temperatures(temperatures):
    total = 0
    count = 0
    highest = float('-inf')
    lowest = float('inf')

    for temp in temperatures:  # iteration
        if temp is not None:   # selection
            total += temp
            count += 1

            if temp > highest:
                highest = temp
            if temp < lowest:
                lowest = temp

    if count > 0:
        average = total / count
        print("\nWeather Analysis:")
        print("Average temperature:", round(average, 2))
        print("Highest temperature:", highest)
        print("Lowest temperature:", lowest)
    else:
        print("No valid temperature data.")

def display_menu():
    print("Choose a location:")
    for i in range(len(locations)):
        print(f"{i+1}: {locations[i][0]}")

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter number: "))
            if 1 <= choice <= len(locations):
                return choice - 1
            else:
                print("Invalid choice. Try again.")
        except:
            print("Please enter a valid number.")


display_menu()
index = get_user_choice()

name, lat, lon = locations[index]
print(f"\nYou selected: {name}")

weather_data = get_weather(lat, lon)

if weather_data:
    temps = weather_data["hourly"]["temperature_2m"]
    analyze_temperatures(temps)
