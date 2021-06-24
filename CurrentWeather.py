import requests,json,random,playsound,os,time

class CurrentWeather:
  def getCurrentTemp():
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY = os.environ['OpenWeather_API_Key']
    CITY = "Shere"
    UNITS = "metric"

    URL = f"{BASE_URL}q={CITY}&appid={API_KEY}&units={UNITS}"

    response = requests.get(URL)
    if response.status_code == 200:
      return response.json()['main']['temp']
    else:
      return response

    print(response)

  def getCurrentWeather():
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY = os.environ['OpenWeather_API_Key']
    CITY = "Shere"
    UNITS = "metric"

    URL = f"{BASE_URL}q={CITY}&appid={API_KEY}&units={UNITS}"

    response = requests.get(URL)
    if response.status_code == 200:
      return response.json()['weather'][0]['description']
    else:
      return response

