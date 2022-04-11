import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

# importing the library
import requests
from bs4 import BeautifulSoup


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
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Robo Sir. Please tell me how may I help you")       

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

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")   

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 

        elif 'open leetcode' in query:
            webbrowser.open("leetcode.com")
        
        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")


        elif 'play music' in query:
            # music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            music_dir = 'C:\\Users\\KIIT\\Downloads\\Songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\KIIT\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to naman' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "2005495@kiit.ac.in"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry . I am not able to send this email")    

        elif 'bye bye' in query:
            speak("Bye Bye Sir, Have a good day") 
            break
        
        elif 'shutdown' in query:
            speak("Sir are you sure to turn off the system ?")
            content = takeCommand()
            if content == 'yes':
                speak("System will shutdown in 10 secoends from now.")
                os.system("shutdown /s /t 10")

        elif 'restart' in query:
            speak("Sir are you sure to restart the system ?")
            content = takeCommand()
            if content == 'yes':
                speak("System will restart in 10 secoends from now.")
                os.system("shutdown /r /t 10")

        elif 'temperature' in query:
            speak("Sir for which city ?")
            content = takeCommand()
            if content == 'my city':
                city = "guwahati"
            else :
                print(content)
                city = content
            city = "guwahati" 
            url = "https://www.google.com/search?q="+"weather"+city
            html = requests.get(url).content
            
            soup = BeautifulSoup(html, 'html.parser')
            temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
            str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
            
            # format the data
            data = str.split('\n')
            sky = data[1]
            listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
            strd = listdiv[5].text
            pos = strd.find('Wind')
            other_data = strd[pos:]

            speak("Temperature is")
            speak(temp)
            speak("Sky Description is ")
            speak(sky)
            speak(other_data)
