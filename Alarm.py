import requests,json,random,playsound,os,time
from Speak import Speak
from WeatherPicker import weatherPicker
from CurrentWeather import CurrentWeather


class Alarm:
  def Activate():
    API_KEY = os.environ['IFTTT_Key']
    #Start the light sequence
    requests.get(f"https://maker.ifttt.com/trigger/brightness1/with/key/{API_KEY}") #1st brightness
    requests.get(f"https://maker.ifttt.com/trigger/ledwhite/with/key/{API_KEY}") #colour
    requests.get(f"https://maker.ifttt.com/trigger/deskledon/with/key/{API_KEY}") #Turn on
    for i in range(1,11):
      requests.get(f"https://maker.ifttt.com/trigger/brightness{i}/with/key/{API_KEY}")
      time.sleep(5)
    playsound.playsound("alarmSound.mp3") #Alarm sound
    time.sleep(15)
    
    Speak.Speak("Good Morning!")
    time.sleep(2)
    Speak.Speak(f"The tempreture in London is {CurrentWeather.getCurrentTemp()} with {CurrentWeather.getCurrentWeather()}. {weatherPicker.PickPhrase()}")
    
    time.sleep(600)

    requests.get(f"https://maker.ifttt.com/trigger/deskledoff/with/key/{API_KEY}")