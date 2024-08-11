import datetime
import os
import webbrowser
import random
import cv2
import sys
import time
import operator
import pyttsx3
import pyautogui
import pyjokes
import pywhatkit as kit
import speech_recognition as sr
from wikipedia import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
        hour = int(datetime.datetime.now().hour)


        if hour >= 0 and hour < 12:
            speak("Good Morning! ")
        elif hour >= 12 and hour < 18:
            speak("Good Afternoon! ")
        else:
            speak("Good Evening! ")
        speak(" i am paanntti what can i do for you ")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
     query = takeCommand().lower()
     if'jarvis' in query:
      print ("yess vanshika")
      speak("yess vanshika")

     elif "what is your name" in query:
      print('My Name Is Jarvis')
      speak('My Name Is Jarvis')
      print('I can Do Everything that my creator programmed me to do')
      speak('I can Do Everything that my creator programmed me to do')

     elif "who created you" in query:
      print('My creater Team Jarvis , I was created with Python Language, in Py Charm.')
      speak('My creater Team Jarvis, I was created with Python Language, in py charm.')

     elif 'google it ' in query:
      speak('Searching Wikipedia...')
      query = query.replace("google it", "")
      results = wikipedia.summary(query, sentences=2)
      speak("According to Wikipedia")
      print(results)
      speak(results)

     elif'just open google' in query:
      webbrowser.open('google.com')
     elif'open google' in query:
      speak("what should i search?")
      qry = takeCommand().lower()
      webbrowser.open(f"(qry)")
      results = wikipedia.summary(qry, sentances=2)
      speak(results)

     elif 'close google' in query:
       os.system("taskkill /f /im msedge.exe")

     elif 'search on youtube' in query:
      query = query.replace("search on youtube", "")
      webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

     elif 'open youtube' in query:
         speak("what you will like to watch ?")
         qrry = takeCommand().lower()
         kit.playonyt(f"{qrry}")

     elif 'close chrome' in query:
         os.system("taskkill /f /im chrome.exe")

     elif 'close youtube' in query:
         os.system("taskkill /f /im msedge.exe")

     elif "open visual studio" in query:
         npath = "C:\\Users\\Vanshika Mishra\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         os.startfile(npath)
     elif "close visual studio" in query:
         os.system("taskkill /f /im Code.exe")

     elif "open chrome" in query:
         npath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
         os.startfile(npath)
     elif "close chrome" in query:
         os.system("taskkill /f /im chrome.exe")

     elif "open edge" in query:
         npath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
         os.startfile(npath)
     elif "close edge" in query:
         os.system("taskkill /f /im msedge.exe")

     elif "open command prompt" in query:
         os.system("start cmd")
     elif "close command prompt" in query:
         os.system("taskkill /f /im cmd.exe")

     elif 'play music' in query:
         music_dir = ''
         songs = os.listdir(music_dir)
         os.startfile(os.path.join(music_dir, random.choice(songs)))
     elif 'close music' in query:
         os.system("taskkill /f /im vlc.exe")

     elif 'what is the time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f" the time is {strTime}")
         print(f" the time is {strTime}")

     elif "shut down the system" in query:
        os.system("shutdown /s /t 5")

     elif "restart the system" in query:
        os.system("shutdown /r /t 5")

     elif "Lock the system" in query:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

     elif "go to sleep" in query:
         speak(' alright then, I am switching off')
         sys.exit()

     elif "open camera" in query:
         cap = cv2.VideoCapture(0)
         while True:
             ret, img = cap.read()
             cv2.imshow('camera', img)
             k = cv2.waitKey(50)
             if k == 27:
                 break;
         cap.release()
         cv2.destroyAllWindows()

     elif "tell me a joke" in query:
         joke = pyjokes.get_joke()
         speak(joke)

     elif "ip address" in query:
         ip = get('https://api.ipify.org').text
         speak(f"your IP address is {ip}")
         try:
             ipAdd = requests.get('https://api.ipify.org').text
             print(ipAdd)
             speak("your ip adress is")
             speak(ipAdd)
         except Exception as e:
             speak("network is weak, please try again some time later")




     elif "volume up" in query:
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")

     elif "volume down" in query:
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")






