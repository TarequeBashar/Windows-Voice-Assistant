import pyttsx3
import datetime
import speech_recognition as sr 

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():

    time = int(datetime.datetime.now().hour)

    if time >= 0 and time <= 12:
        speak("Good Morning My Friend")

    elif time >= 12 and time <=18:
        speak("Good afternoon my friend")

    else:
        speak("Good Evening my Friend")

    speak("I am your friend Harry Potter  It's my pleasure to hear you again")



def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(query)
        speak(query)

    except Exception as e:
        # print(e)    
        speak("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wish()
    takeCommand()

    
    