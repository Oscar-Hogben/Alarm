print("Loading...")
import requests,json,random,playsound,os,time
from WeatherPicker import weatherPicker
from CurrentWeather import CurrentWeather
from Alarm import Alarm

print("Loaded!")
time.sleep(1)
os.system('clear')

print(CurrentWeather.getCurrentTemp())

print(CurrentWeather.getCurrentWeather())

print(weatherPicker.Sunny_Cold())