import requests,json,random,playsound,os,time
from CurrentWeather import CurrentWeather


class weatherPicker:
  def PickPhrase():
    currentTemp = CurrentWeather.getCurrentTemp()
    currentWeather = CurrentWeather.getCurrentWeather()
    if currentTemp >= 20 and ("clouds" in currentWeather or "clear" in currentWeather):
      responses = ["Perfect for a day at the pool!", "Perfect for some paddleboarding!", "Perfect for a bike ride!", "Perfect for the beach!", "Perfect for some watersports!", "Perfect for a day in guildford!", "Perect to see some friends!"]
    elif currentTemp >= 10 and ("clouds" in currentWeather or "clear" in currentWeather):
      responses = ["Perfect to see some friends!", "Perfect to see some falimy!", "Perfect for a day in guildford!", "Perfect for a cycle ride!", "Perfect for a gaming marathon!", "Perfect for soem programming!", "Perfect to get some work done!"]
    elif currentTemp > 0 and ("clouds" in currentWeather or "clear" in currentWeather):
      responses = ["Perfect for a trip to the cinema!", "Perfet for seeing some family!", "Perfect for seeing some friends!","Perfect for watching a film!", "Perfect for a trip to the supermarket!", "Perfect to get some work done!"]
    elif currentTemp <= 0 and ("clouds" in currentWeather or "clear" in currentWeather):
      responses = ["Perfect for some ice scating!", "Perfect for a frosty walk!", "Perfect to get some work done!", "Perfect to wath a film!"]
    elif "rain" in currentWeather or "mist" in currentWeather:
      responses = ["Perfect to get some work done!", "Perfect to watch a film!", "Perfect to go to the cinema!", "Perfect to do some programming!", "Perfect to have a gaming marathon!"]
    elif "snow" in currentWeather:
      responses = ["Perfect to go sledging!", "Perfect to go on a snowy walk!", "Perfect to build a snowman!", "Perfect to go ice scating!"]
    return random.choice(responses)

  def Sunny_Warm():
    responses = ["Perfect for a day at the pool!", "Perfect for some paddleboarding!", "Perfect for a bike ride!", "Perfect for the beach!", "Perfect for some watersports!", "Perfect for a day in guildford!", "Perect to see some friends!"]
    return random.choice(responses)
  def Rainy():
    responses = ["Perfect to get some work done!", "Perfect to watch a film!", "Perfect to go to the cinema!", "Perfect to do some programming!", "Perfect to have a gaming marathon!"]
    return random.choice(responses)
  def Sunny_Cold():
    responses = ["Perfect for a trip to the cinema!", "Perfet for seeing some family!", "Perfect for seeing some friends!","Perfect for watching a film!", "Perfect for a trip to the supermarket!", "Perfect to get some work done!"]
    return random.choice(responses)
  def Freezing():
    responses = ["Perfect for some ice scating!", "Perfect for a frosty walk!", "Perfect to get some work done!", "Perfect to wath a film!"]
    return random.choice(responses)
  def Snowing():
    responses = ["Perfect to go sledging!", "Perfect to go on a snowy walk!", "Perfect to build a snowman!", "Perfect to go ice scating!"]
    return random.choice(responses)
  def TunderStorm():
    responses = ["Perfect time to watch some thunder!"]
    return random.choice(responses)
