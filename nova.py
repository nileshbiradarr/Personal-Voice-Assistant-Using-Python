import ctypes
import os
import subprocess
import pyttsx3
import datetime
import webbrowser
import pyjokes
import pywhatkit
import smtplib
import requests
import speech_recognition as sr
import wikipedia
import winshell

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)  # engine will speak the audio string that we will pass
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good morning,Sir")

    elif hour >= 12 and hour <= 18:
        speak("Good afternoon,Sir")

    elif hour >= 18 and hour <= 21:
        speak("Good evening,Sir")

    else:
        speak("Have a good night,Sir")
    print("welcome to ramro adik institude of technology. How may I help you ?")
    speak("welcome to ramro adik institude of technology. How may I help you ?")


def takeCommand():
    """
    this function will take the command from the user and then process it accordingly to the need or
    it takes the microphone input from the user and gives a string output
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=5)
        audio = r.listen(source, phrase_time_limit=4)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        print(e)
        print("say that again please...")
        #speak("didn't hear it clear, can you please say it again")
        return "none"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sfxtrials18@gmail.com', 'Trialssfx@18')
    server.send('sfxtrials18@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    # speak("hello! how are you doing ")
    wishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)


        elif "course " in query:
            print("Bachelor of Technology , Bachelor of Architecture , Bachelor of Computer Applications , Information Technology  , Nursing , Bachelor of Pharmacy. ")
            speak("i am fine .How are you, Sir")

           

        elif 'open collage website' in query:
            webbrowser.open("dypatil.edu")


        elif ' stack overflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'nova open twitter' in query:
            webbrowser.open("twitter.com")


        elif 'nova open instagram' in query:
            webbrowser.open("instagram.com")


        elif 'nova open facebook' in query:
            webbrowser.open("facebook.com")


        elif 'nova play' in query:
            song = query.replace('play', '')
            speak('playing..' + song)
            print(song)
            pywhatkit.playonyt(song)

        elif 'nova time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('current time is: ' + time)
            print(time)

        elif 'nova joke' in query:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())

        elif 'nova open pycharm' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.1\\bin\\pycharm64.exe"
            os.startfile(codePath)


        elif ' open chrome' in query:
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)


        elif 'nova open valorant' in query:
            codePath = "C:\\Riot Games\\Riot Client\\RiotClientServices.exe"
            os.startfile(codePath)


        elif 'email to phantom' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = "phantomphoenix1544@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent! successfully")

            except Exception as e:
                print(e)
                speak("Sorry, Sir I couldn't send the email")


        elif "how are you" in query:
            print("i am fine .How are you, Sir")
            speak("i am fine .How are you, Sir")

        elif " Artificial intelligence" in query:
            print("Artificial intelligence is the simulation of human intelligence processes by machines, especially computer systems. Specific applications of AI include expert systems, natural language processing, speech recognition and machine vision.")
            speak("Artificial intelligence is the simulation of human intelligence processes by machines, especially computer systems. Specific applications of AI include expert systems, natural language processing, speech recognition and machine vision.")


        elif "fine" in query or "good" in query:
            speak("It's good to know that your fine")


        elif "who are you" in query:
            print("I am your virtual assistant created by Mr.sam")
            speak("I am your virtual assistant created by Mr.sam")

        elif 'reason for you' in query:
            print("I was created as a Mini project by samit,nilesh and deepesh")
            speak("I was created as a Mini project by samit,nilesh and deepesh")


        elif 'nova lock windows' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()


        elif "nova hibernate windows" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")


        elif 'nova shutdown windows' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'nova empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        # elif "camera" in query or "take a photo" in query:
        #     ec.capture(0, "nova Camera ", "img.jpg")

        elif "nova restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "nova Good Morning" in query:
            speak("A warm" + query)
            speak("How are you Mister")


        elif 'nova close' in query:
            speak("Thanks for giving me your time")
            exit()