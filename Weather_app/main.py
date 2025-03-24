import requests
import json
import os
import win32com.client as wincl
 
city = input("Enter city name: ")
url = f"http://api.weatherapi.com/v1/current.json?key=cbac537e6b7c4b91a6f160132252403&q={city}"

r = requests.get(url)
 
wdic = json.loads(r.text)
print("City:", wdic["location"]["name"])
print("Region:", wdic["location"]["region"])
print("Country:", wdic["location"]["country"])
print("Local Time:", wdic["location"]["localtime"])
print("Temperature (°C):", wdic["current"]["temp_c"])
print("Condition:", wdic["current"]["condition"]["text"])

speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak(f"City: {wdic['location']['name']}")
speak.Speak(f"Region: {wdic['location']['region']}")
speak.Speak(f"Country: {wdic['location']['country']}")
speak.Speak(f"Local Time: {wdic['location']['localtime']}")
speak.Speak(f"Temperature: {wdic['current']['temp_c']} degree Celsius")
speak.Speak(f"Condition: {wdic['current']['condition']['text']}")
