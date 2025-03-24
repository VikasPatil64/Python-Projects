import requests
import json
import win32com.client as wincl
import os

def get_weather(api_key, city):
    """Fetch weather data from WeatherAPI.com"""
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for HTTP failures
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def speak_weather(weather_data):
    """Announce weather using text-to-speech"""
    speak = wincl.Dispatch("SAPI.SpVoice")
    location = weather_data['location']
    current = weather_data['current']
    
    weather_report = (
        f"Weather in {location['name']}, {location['country']}: "
        f"Temperature is {current['temp_c']}°C, "
        f"Condition: {current['condition']['text']}. "
        f"Local time is {location['localtime']}."
    )
    
    print("\n=== Weather Report ===")
    print(f"City: {location['name']}")
    print(f"Region: {location['region']}")
    print(f"Country: {location['country']}")
    print(f"Local Time: {location['localtime']}")
    print(f"Temperature: {current['temp_c']}°C")
    print(f"Condition: {current['condition']['text']}\n")
    
    speak.Speak(weather_report)

def main():
    os.system("cls")
    print("=== Python Weather App ===")
    
    # Note: Store API keys securely (use environment variables in real projects)
    API_KEY = "cbac537e6b7c4b91a6f160132252403"
    
    city = input("Enter city name: ")
    weather_data = get_weather(API_KEY, city)
    
    if weather_data:
        speak_weather(weather_data)
    else:
        print("Failed to fetch weather data. Please try again.")

if __name__ == "__main__":
    main()