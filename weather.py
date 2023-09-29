import requests
import json

# OpenWeatherMap API key
API_KEY = "2b2f7322544025e1ef21e64673e44e08"

# Function to fetch weather data from the API
def get_weather(city_name):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city_name, "appid": API_KEY, "units": "metric"}  # Use metric units for Celsius

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] == 200:
            return data
        else:
            print("Error: Unable to fetch weather data.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to display weather information
def display_weather(weather_data):
    if weather_data:
        city = weather_data["name"]
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description.capitalize()}")
    else:
        print("No weather data available.")

# Main function
def main():
    print("Welcome to the Weather App")
    city_name = input("Enter the name of a city: ")

    weather_data = get_weather(city_name)

    display_weather(weather_data)

if __name__ == "__main__":
    main()
