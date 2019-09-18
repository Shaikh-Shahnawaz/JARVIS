import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
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
        speak("Good Evening")

    speak("I am Jarvis Sir. Please tell me how may I help you") 

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:    
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query 

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shaikhshahnawaz8821@gmail.com', 'shahnawaz742454')
    server.sendmail('shaikhshahnawaz8821@gmail.com', to, content)
    server.close()





if __name__ == "__main__":
    wishMe()
    while True:
         query = takeCommand().lower()


         if 'wikipedia' in query:
            speak ('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)


         elif 'open youtube' in query:
             webbrowser.open("https://www.youtube.com")

         elif 'open google' in query:
             webbrowser.open("https://www.google.com")

         elif 'open amazon' in query:
             webbrowser.open("https://www.amazon.in")

         elif 'open facebook' in query:
             webbrowser.open("https://www.facebook.com/?ref=tn_tnmn")

         elif 'open instagram' in query:
             webbrowser.open("https://www.instagram.com/?hl=en")
             
         elif 'open stackoverflow' in query:
             webbrowser.open("stackoverflow.com")

         elif 'open my gmail' in query:
             webbrowser.open("https://mail.google.com/mail/u/0/#sent")

         elif 'play dilbar on youtube' in query:
             webbrowser.open("https://www.youtube.com/watch?v=TRa9IMvccjg")    

         elif 'play o saki saki on youtube' in query:
             webbrowser.open("https://www.youtube.com/watch?v=6wNFJIbTxNk")

         elif 'play machayenge on youtube' in query:
             webbrowser.open("https://www.youtube.com/watch?v=7tNPxY_ntEA")    

         elif 'play atif aslam songs on youtube' in query:
             webbrowser.open("https://www.youtube.com/watch?v=tNxJBWcll3Y")

         elif 'play kabir singh songs on youtube' in query:
             webbrowser.open("https://www.youtube.com/watch?v=BDlNjOc3wiQ")                 


         elif 'play music' in query:
             music_dir = 'D:\\Songs'
             songs = os.listdir(music_dir)
             print(songs)
             os.startfile(os.path.join(music_dir, songs[8]))


         elif 'the time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"sir, the time is {strTime}")

         elif 'open pubg' in query:
             pubgPath = "E:\\program files\\txgameassistant\\appmarket\\AppMarket.exe"
             os.startfile(pubgPath)


         elif 'email to shanu' in query:
             try:
                speak("What should I say?")
                content = takeCommand()
                to = "shahnawazkhan8821@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
             except Exception as e:
                 print(e) 
                 speak("sorry shanu. I am not able to send this email")

         elif 'quit' in query:
             exit()        

                      


             

             




