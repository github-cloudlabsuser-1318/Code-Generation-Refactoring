import requests
import os

API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        condition = data['weather'][0]['description']
        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {condition}")
    else:
        print("Failed to retrieve weather data. Check the city name or API key.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)