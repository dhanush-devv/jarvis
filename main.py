import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os


recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi="f7975234d7f54911a209cb96ff27385d"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
     tts = gTTS(text)
     tts.save('temp.mp3')
      # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def aiProcess(command):
    client=OpenAI(
    api_key="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"
)

    completion=client.chat.completions.create(
        model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses"},
        {"role": "user", "content": command}
    ]
    )
    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtub" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startsWith("play"):
        song=c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")

        if r.status_code==200:
            data=r.json()

            articles=data.get("articles",[])

            for article in articles:
                speak(article['title'])
    
    else:
        #Openai
        output=aiProcess(c)
        speak(output)




if __name__=="__main__":
    speak("Initializing Jarvis...")
    while True:
        #listen for wake work Jarvis
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        
        
        print("recognizing....")
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening...!")
            audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word=r.recognize_google(audio)
            print(word)
            if(word.lower()=="jarvis"):
                speak("Yes")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...!")
                    audio = r.listen(source)
                    command=r.recognize_google(audio)

                    processCommand(command)

        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except Exception as e:
            print("Error; {0}".format(e))
