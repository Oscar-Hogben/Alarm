print("Loading...")
import requests,json,random,playsound,os,time, datetime
from gtts import gTTS
from WeatherPicker import weatherPicker
from CurrentWeather import CurrentWeather
from Alarm import Alarm
from Speak import Speak

print("Loaded!")
time.sleep(1)
os.system('clear')

while True:
  time.sleep(1)

  os.system("clear")

  date_time = str(datetime.datetime.now().strftime("%H:%M"))
  file = open("alarmTime.txt", "r")
  alarm_time_str = file.read()

  if date_time == alarm_time_str:
    print("Alarm")
    Alarm.Activate()
  else:
    print(date_time)
    print(alarm_time_str)
    print("Looping")
    
    


