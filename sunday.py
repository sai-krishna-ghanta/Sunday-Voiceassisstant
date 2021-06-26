import warnings
import pyautogui
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import time
import requests
import os
from googletrans import Translator
from pyautogui import click
from keyboard import press,write
from time import sleep
from PyDictionary import PyDictionary
import speedtest
import eel
import cv2
import random


eel.init("project")

warnings.filterwarnings("ignore")
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)  #changing index , changes voices, 1 for female and 0 for male

def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        eel.addText("Listening....")
        talk("Speak now")
        audio = r.listen(source)
        try:
            global speech
            speech=" "
            speech = r.recognize_google(audio)
            speech = speech.lower()
            eel.addText("You said: "+speech)
        except sr.UnknownValueError:
            x = "Sorry,I couldn't hear you"
            talk(x)
            eel.addText(x)
        except sr.RequestError:
            talk("Sorry , My API to recognize voice is down")
    return speech

def get_audio_telugu():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        eel.addText("Listening....")
        talk("Speak now")
        audio = r.listen(source)
        try:
            global speech
            speech=" "
            speech = r.recognize_google(audio,language='te-IN')
            speech = speech.lower()
            eel.addText("You said: "+speech)
        except sr.UnknownValueError:
            x = "Sorry,I couldn't hear you"
            talk(x)
            eel.addText(x)
        except sr.RequestError:
            talk("Sorry , My API to recognize voice is down")
    return speech

def get_audio_hindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        eel.addText("Listening....")
        talk("Speak now")
        audio = r.listen(source)
        try:
            global speech
            speech=" "
            speech = r.recognize_google(audio,language='hi')
            speech = speech.lower()
            eel.addText("You said: "+speech)
        except sr.UnknownValueError:
            x = "Sorry,I couldn't hear you"
            talk(x)
            eel.addText(x)
        except sr.RequestError:
            talk("Sorry , My API to recognize voice is down")
    return speech

def today_date():
    date = str(datetime.datetime.now().date())
    hour = str(datetime.datetime.now().hour)
    min = str(datetime.datetime.now().minute)
    sec = str(datetime.datetime.now().second)
    time=date+" "+hour+"hours "+min+"minutes "+sec+"seconds"
    return time

def wiki(text):
    text = text.replace("wikipedia"," ")
    text = text.replace("Sunday"," ")
    results = wikipedia.summary(text , sentences=3)
    return results

def WhatsappMsg(name,message):
     
    webbrowser.open("https://web.whatsapp.com/")

    sleep(15)

    buttonlocation = pyautogui.locateOnScreen('search.png')
    buttonpoint = pyautogui.center(buttonlocation)
    buttonx, buttony = buttonpoint
    click(buttonx,buttony)
    sleep(1)

    write(name)
    sleep(2)
    
    buttony+=150
    click(buttonx,buttony)
    sleep(0.5)
    
    write(message)
    press('enter')

def WhatsappChat(name): 

    webbrowser.open("https://web.whatsapp.com/")

    sleep(10)

    buttonlocation = pyautogui.locateOnScreen('search.png')
    buttonpoint = pyautogui.center(buttonlocation)
    buttonx, buttony = buttonpoint
    click(buttonx,buttony)

    sleep(1)

    write(name)

    sleep(2)

    buttony+=150
    click(buttonx,buttony)

def weather(location):
    user_api =  "551fa158b9c984913a5f0b943e7e8578"
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = str(api_data['main']['humidity'])
    wind_spd = str(api_data['wind']['speed'])
    date = str(datetime.datetime.now().date())
    print("Weather Stats for - "+date)
    print("Current temperature is: {:.2f} deg C".format(temp_city))
    print("Current weather desc  :",weather_desc)
    print("Current Humidity      :",hmdt, '%')
    print("Current wind speed    :",wind_spd ,'kmph')
    eel.addText("Weather Stats for - "+date)
    eel.addText("Current temperature is: {:.2f} deg C".format(temp_city))
    eel.addText("Current weather desc  :"+weather_desc)
    eel.addText("Current Humidity in %     :"+hmdt)
    eel.addText("Current wind speed  in kmph :"+wind_spd)
    return temp_city

def OnlineClass(x):
    link1 = 'https://iiitnr.webex.com/webappng/sites/iiitnr/meeting/info/0fc0da5861fa4f51ba3e96c982d5768e?MTID=m894df52c17e081a5c48e42ece17a3e54&siteurl=iiitnr&meetingAuthToken=QUhTSwAAAAW1cbpsatbuyOG%2FX8j5A3RyKJ0iPxE7FUkLCpbpr7LAdpXHdsM2mk5ZaToHy%2FHCbwti4%2FZ8YHgk9B5921uKiZ6CCU6FMNoxoFhjt9PBYhCSIbYcMIYkITk0byXkrkxBjYaOBU%2F3afwlRDMKXNseUysftkN6UGG1d1F361sBrsjicEfGiMcK1ID19%2BnFDHvpdEVVmIp51o06xfctYDIojK6pn6a914DkYSbk%2BcZek9E%2B5Q%3D%3D'
    link2 = 'https://iiitnr.webex.com/webappng/sites/iiitnr/meeting/download/228178a0aac94299b9f6d015efecd2ce?siteurl=iiitnr&MTID=m73189c24c37347f4cf5b22df6310cc14'
    if "sensors" in x or "statistics" in x or "Workshop" in x or "English":
        webbrowser.open(link1)
    if "things" in x:
        webbrowser.open(link2)
    sleep(5)
    buttonlocation = pyautogui.locateOnScreen('join.png')
    buttonpoint = pyautogui.center(buttonlocation)
    buttonx, buttony = buttonpoint
    click(buttonx,buttony)
    sleep(7)

def trans_hindi():
    translator = Translator(service_urls=['translate.googleapis.com'])
    talk("what to translate")
    trans_ = get_audio_hindi()
    results = translator.translate(trans_)
    Text = results.text
    talk(Text)
    eel.addText("Translated    words are  - "+Text)

def trans_telugu():
    translator = Translator(service_urls=['translate.googleapis.com'])
    talk("what to translate")
    trans_ = get_audio_telugu()
    results = translator.translate(trans_)
    Text = results.text
    talk("Translated"+Text)
    eel.addText("Translated    words are  - "+Text)

def SpeedTest():

    talk("Checking speed")
    st = speedtest.Speedtest()
    st.get_best_server()
    downloding = st.download()
    correctDown = float(downloding/800000)
    uploading = st.upload()
    correctUp = float(uploading/800000)
    eel.addText("Downloading in Mb/S     :::       "+str(correctDown))
    eel.addText("Uploading Speed in Mb/S :::       "+str(correctUp))

def camera_normalpicture():
    talk("Capturing Image")
    eel.addText("Captured an image")
    webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW) # reading frames CAP_DSHOW is just as per documentation which clears the bug in backend of opencv
    ret, frame = webcam.read()# Checking if frame captured or not
    webcam.release()    # releasing the webcam
    cv2.imshow("my image", frame)    # displaying image
    cv2.waitKey()# stopping the output
    cv2.destroyAllWindows() # releasing all windows

def camera_grayscale():
    talk("Capturing gray scale Image")
    eel.addText("Captured an Gray scale image")
    webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    ret, frame = webcam.read()
    webcam.release()    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("my image", frame)   
    cv2.waitKey()
    cv2.destroyAllWindows() 

def dict():
    dictionary=PyDictionary()
    talk("Dictionary activated Sir  ")
    eel.addText("Dictionary activated Sir")
    talk("What should I do now")
    eel.addText("What should I do now")
    record = get_audio()

    if "meaning" in record:
        talk("For which word")
        meaningword = get_audio()
        out = dictionary.meaning(meaningword)
        eel.addText(str(out))
        talk(out)

    elif "synonym" in record:
        talk("For which word")
        synonymword = get_audio()
        out = dictionary.synonym(synonymword)
        eel.addText(str(out))
        talk(out)

    elif "antonym" in record:
        talk("For which word")
        antonymword = get_audio()
        out = dictionary.antonym(antonymword)
        eel.addText(str(out))
        talk(out)
    
    else:
        talk("Sorry , I can't find this")
        eel.addText("Sorry , I can't find this")

def coin_toss():

    talk("I am going to flip coin")
    result = random.choice(["Heads","Tails"])
    talk(result)
    eel.addText(result)
    
@eel.expose
def trail():
    eel.addText("Hello this is Sunday , the voice assisstant")
    talk("Hello this is Sunday , the voice assisstant")
    while True:
        text = get_audio()
        text = text
        speak = "Sorry, I don't have reply for this"

        if "time" in text:
            X = today_date()
            speak = X
                    
        elif "wikipedia" in text or "Wikipedia" in text:
            speak = wiki(text)
                    
        elif "who are you" in text or "define yourself" in text:
            speak = """Hello, I am sunday,The Voice assisstant. 
            I was created by Avinash , Sai Krishna , Supriya"""
            
        elif "your name" in text:
            speak = "This is Sunday."
    
        elif "who am i" in text:
            speak = "You might be a human."
            
        elif "why do you exist" in text or "why did you come" in text:
            speak = "It is a secret."
    
        elif "how are you" in text:
            speak =  "I am fine, Thank you!"
            speak += "\nHow are you?"
                    
        elif "i am good" in text or "i am fine" in text:
            speak  ="cool , How can i help for you"
                    
        elif "i am fine" in text :
            speak = "It's good to know that you are fine"
        
        elif 'news' in text:
            news = webbrowser.open("https://timesofindia.indiatimes.com/home/headlines")
            talk('Here are some headlines from the Times of India,Happy reading')
            speak = " "
            
        elif "open" in text.lower():                
            if "youtube" in text.lower():
                speak = "opening youtube in browser"
                webbrowser.open("https://youtube.com/")
            
            elif "facebook" in text.lower():
                speak = "opening facebook in browser"
                webbrowser.open("https://www.facebook.com/")

            elif "instagram" in text.lower():
                speak = "opening instagram in browser"
                webbrowser.open("https://www.instagram.com/")
                
            elif "google" in text.lower():
                speak = "opening google in browser"
                webbrowser.open("https://google.com")
            
            elif "whatsapp" in text.lower():
                speak = "opening whatsapp in browser"
                webbrowser.open("https://web.whatsapp.com/")
                
            elif "github" in text.lower():
                speak = " opening github"
                webbrowser.open("https://github.com")

            elif "profile" in text.lower() or "repository" in text.lower():
                speak = "So you are going to see my profile and my code"
                webbrowser.open("https://github.com/sai-krishna-ghanta/Sunday-Voiceassisstant")  

            elif "word" in text.lower():
                speak = "Opening wordfile"
                os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.exe")

            elif "note" in text.lower():
                speak = "Opening wordfile"
                os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\ONENOTE.exe")
        
            elif "power" in text.lower() or "point" in text.lower():
                speak = "Opening Power point presentation "
                os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.exe")


            elif "notepad" in text.lower():
                speak = "Opening notepad "
                os.startfile(r"C:\Windows\system32\notepad.exe")
                
            elif "code" in text.lower():
                speak = "Opening VS code"
                os.startfile(r"C:\Users\skgha\AppData\Local\Programs\Microsoft VS Code\Code.exe")


            else:
                speak = "No such Application in framework "
                
        elif "youtube" in text.lower():
            ind = text.lower().split().index("youtube")
            search = text.split()[ind + 1:]
            webbrowser.open("https://www.youtube.com/results?search_query=" + "+".join(search))
            speak ="opening" + str(search) +  " on youtube "
                        
        elif "search" in text.lower():
            x = text.lower().split().index("search")
            y = text.split()[x + 1:]
            webbrowser.open("https://www.google.com/search?q="+"+".join(y))    
            speak ="searching" + str(y) + " on google"
                    
        elif "where is" in text:
            a =  text.lower().split().index("is")
            location = text.split()[a +1: ]
            speak ="searching for "+str(location)
            webbrowser.open("https://www.google.com/maps/place/"+"+".join(location))
                         
        elif "don't listen" in text or "stop listening" in text or "do not listen" in text:
            talk("for how many seconds do you want me to sleep")
            eel.addText("for how many seconds do you want me to sleep")
            a = int(get_audio())
            time.sleep(a)
            speak = str(a) + " seconds completed. Now you can ask me anything"
                    
        elif "whatsapp" in text :
            if "message" in text:
                eel.addText("What's the name of person?")
                talk("What's the name of person")
                name = get_audio()
                eel.addText("What's the message you wanna send?")
                talk("What's the message you wanna send")
                message = get_audio()
                talk("Opening whatsapp web")
                WhatsappMsg(name,message)
                talk("Done")
                break

            elif "chat" in text:
                eel.addText("What's the name of person?")
                talk("What's the name of person")
                name = get_audio()
                talk("Opening chat")
                WhatsappChat(name)
                talk("Done")
                break

        #elif "Hi" or "Hello" or "hi" or "hello" in text:
             #speak ="Hello, it's my pleasure to talk with you"
        
        elif "weather" in text or "climate" in text:
            talk("What is the location ")
            Location = get_audio()
            weather(Location)
            speak = " "

        elif "goodbye" in text or "bye" in text or "quit" in text or "exit" in text:
            eel.addText("Terminating Sunday")
            talk("Terminating Sunday")
            speak = " "
            break

        elif "class" in text:
            talk("Which Subject do you want to attend")
            x= get_audio()
            OnlineClass(x)
            speak = " "

        elif "translate" in text:
            talk("In which Language I need to translate")
            eel.addText("In which Language I need to translate")
            lang = get_audio()
            lang = lang.lower()
            if "hindi" in lang:
                trans_hindi()
            if "telugu" in lang:
                trans_telugu()
            speak = " "

        elif "speed" in text:
            SpeedTest()
            speak = " "

        elif "capture" in text or "image" in text or "webcam" in text:
            talk("which type of image you need")
            eel.addText("Which type of image you need ")
            type_ = get_audio()
            if "color" in type_ or "colour" in type_:
                camera_normalpicture()
                speak = " " 
            if "gray" in type_ or "grey" in type_ or "scale" in type_:
                camera_grayscale()
                speak = " " 

        elif "dictionary" in text:
            dict()
            speak=" "

        elif "coin" in text or "toss" in text or "flip" in text:
            coin_toss()
            speak= " "

        elif "shutdown" in text or "power" in text:
            talk("Would you like to shutdown PC")
            eel.addText("Would you like to shutdown PC")
            shutdown = get_audio()
  
            if shutdown == 'no':
                eel.addText("Request Cancelled")
                talk("request cancelled")
                exit()
            else:
                talk("Shuting down PC")
                os.system("shutdown /s /t 1")

        eel.addText(speak)
        talk(speak)

eel.start("project.html",size=(500, 500))