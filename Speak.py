import requests,json,random,playsound,os,time
from gtts import gTTS

class Speak:
  def Speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    audio_file = 'audio-' + "speach" + ('.mp3')
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(f"Playing: {audio_string}")
    os.remove(audio_file)