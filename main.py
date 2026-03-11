import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary


recognizer=sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

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
