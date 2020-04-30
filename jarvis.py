import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import numpy as np
import cv2
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Rakesh Shrestha")
        speak("I am Unknown Beginner")
        speak(" please tell me how may I help you?")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")
        speak("Who are you?")
        speak(" Please tell me how may I help you?")

    else:
        speak("Good Evening! Mr Rakesh Shrestha")
        speak("I am Unknown Beginner")
        speak(" Please tell me how may I help you?")
def takeCommand():
    #It takes microphone input from the user and returns string output

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
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def closeFile():
        #It takes microphone input from the user and returns string output

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
        # print(e)
        print("Say that again please...")
        speak('Say that again please')
        return "None"
    return query


if __name__ == "__sub_main__":
      wishMe()
      while True:
    # if 1:
        query = closeFile().lower()



        # Logic for executing tasks based on query
        if 'close viber' in query:
            speak('Closing Viber.....')
            os.system('TASKKILL /F /IM Viber.exe')






def open_application(input):
    if "chrome" in input:
        speak("Google Chrome")
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe') #use your drive to open exe or other file
        return
    elif "firefox" in input or "mozilla" in input: #input to get from user i.e. code word
        speak("Opening Mozilla Firefox")
        os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe') #use your drive to open exe or other file
        return
    elif "word" in input:
        speak("Opening Microsoft Word")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Word 2013.lnk')
        return
    elif "excel" in input:
        speak("Opening Microsoft Excel")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Excel 2013.lnk')
        return
    else:
        assistant_speaks("Application not available")
        return









if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()



        # Logic for executing tasks based on query
        #uses internet to search over web
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('Searching youtube....')
            webbrowser.open("youtube.com")



        elif ('open stackoverflow') in query:
            webbrowser.open("stackoverflow.com")










#this method for opening files and document locating your directories

        elif 'play music' in query:
            music_dir = 'E:\\Music'
            speak('Searching music in your folder....')
            songs = os.listdir(music_dir)
            print (songs)
            os.startfile(os.path.join(music_dir, songs[random.randint(1,100)]))



        elif 'next' in query:
            music_dir= 'E:\\Music'
            x = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, x[random.randint(1,100)]))



        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open torrent' in query:
            speak('Just wait i am searching and opening torrent....')
            codePath = "C:\\Users\\HP\\AppData\\Roaming\\uTorrent\\uTorrent.exe"
            os.startfile(codePath)

        elif 'open virtual box' in query:
            codePath = "C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe"
            os.startfile(codePath)


        elif 'open whatsapp' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(codePath)

        elif 'open google chrome' in query:
            speak('Searching google chrome....')
            codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)

        elif 'open photoshop' in query:
            speak('Searching photoshop....')
            codePath =  "D:\\Software\\photoshop\\Photoshop.exe"
            os.startfile(codePath)


        elif 'play minecraft' in query:
            speak('Searching minecraft....')
            codePath = "C:\\Users\\HP\\AppData\\Roaming\\.minecraft\\Launcher.exe"
            os.startfile(codePath)


        elif 'play farcry 4' in query:
            codePath = "C:\\Program Files (x86)\\Mr DJ\\Far Cry 4\\bin\\FarCry4.exe"
            os.startfile(codePath)


        elif 'open viber' in query:
            speak('Just wait Sir, i am opening viber....')
            codePath ="C:\\Users\\HP\\AppData\\Local\\Viber\\Viber.exe"
            os.startfile(codePath)

        elif 'photo' in query:
           speak('Just wait Sir, I am opening  photos folder')
           codePath = "E:\\Sabitri Wedding"
           os.startfile(codePath)

     #open video file
     #this need to modified
        elif 'funny video' in query:
            cap=cv2.VideoCapture('hello.mp4')
            while(True):
             ret, frame=cap.read()
             cv2.imshow('output',frame)
             if (cv2.funnyvideo & 0xFF == stop):
                break
            cap.release()
            cv2.destroyAllWindows


        elif 'my computer' in query:
            codePath =""
            os.startfile(codePath)

        elif 'suyog' in query:
            codePath = "E:\\Suyog ----------  Bartabandan"
            os.startfile(codePath)









    #Chat Bots (use word to have reply uses random selection)


        elif 'who are you' in query:
            speak('My name is Unknown Beginner. I am an personal assistant of Mr. Rakesh Shrestha. You can call me as UB in short. I am here to make your work easy. How about you?')
            continue

        elif 'jarvis' in query:
            spak=['Yes, What happened?','Yes boss, How may I help you?','Yes, What happened Sir?  Can i help you?']
            se=random.choice(spak)
            speak(se)
            continue

        elif 'hello' in query:
           sak=['Hello there! How are you?', 'Hello sweety. How are you?', 'Hi there, how can I help?']
           e=random.choice(sak)
           speak(e)
           continue

        elif 'hi' in query:
            sak=['Hello! there', 'Good to see you again!', 'Hi there, how can I help?']
            e=random.choice(sak)
            speak(e)
            continue


        elif 'how are you' in query:
            sak=['I am okay. How about you?', 'I am fine. How about you?','Good. How are you?']
            e=random.choice(sak)
            speak(e)
            continue

        elif 'boring' in query:
            sak=['Is it?','I dont feel so?','Sir you should travel new place','I will suggest you to sleep.']
            e=random.choice(sak)
            speak(e)


    # continue as your wish to have endless conversation
        elif 'exit' in query:
            speak('By Mr. Rakesh Shrestha. Happy to help you. we will meet you next time. Thank you')
            exit()












