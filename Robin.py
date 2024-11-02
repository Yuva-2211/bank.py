import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia

recognizer = sr.Recognizer()   # for recognisation 
engine = pyttsx3.init()        # initialising pyttsx3
rate = engine.getProperty('rate') # setting up the text rate  
engine.setProperty('rate', + 170)
def speak(text):          # setuping speak function 
    engine.say(text)
    engine.runAndWait()

def algo(command): # recognises commands and does the work
    command = command.lower()  
    if "open google" in command:
        webbrowser.open("https://www.google.com")     
    elif "open instagram" in command:
        webbrowser.open("https://www.instagram.com")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
    elif "open linkedin" in command:
        webbrowser.open("https://in.linkedin.com")
    elif "open amazon" in command:
        webbrowser.open("https://www.amazon.in")
    elif "open flipkart" in command:
        webbrowser.open("https://www.flipkart.com/")
    elif "open Github" in command:
        webbrowser.open("https://github.com")
    elif "new tab" in command:
        webbrowser.open_new_tab
    elif "wikipedia" in command:
        speak("Searching..")
        command = command.replace("wikipedia" ," ")
        result = wikipedia.summary(command , sentences = 2)
        speak("according to wikipedia")
        speak(result)
    else:
        speak("Sorry")

if __name__ == "__main__": 
    speak("Robin here!!")
    while True: # to loop it
        print("Hmm...")
        try:
            with sr.Microphone() as source: # using systems microphone as source
                print("Listening.....")
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=3)

            word = recognizer.recognize_google(audio) # using google cloud for speech recognition 
            if word.lower() == "hey robin" or word.lower() == "robin": # the wake up command
                speak("Yes")
                with sr.Microphone() as source:
                    print("active")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    algo(command)  
#error handling
        except sr.UnknownValueError:
            print("Sorry ")
        except sr.RequestError as e:
            print(f"soory {e}")
        except Exception as e:
            print(f"Error: {e}")
