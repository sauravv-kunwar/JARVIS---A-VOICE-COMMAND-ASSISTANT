import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open chatgpt" in c.lower():
        webbrowser.open("https://chatgpt.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open github" in c.lower():
        webbrowser.open("https://github.com") 
        
    elif c.lower().startswith("play"):
        try:
            song = c.lower().split(" ", 1)[1]  # Handles multi-word songs
            link = musiclibrary.music.get(song)
            if link:
                webbrowser.open(link)
            else:
                speak(f"Sorry, I couldn't find the song {song}")
        except IndexError:
            speak("Please say the song name after 'play'.")

    else:
        speak("I did not understand that command.") 


if __name__ == "__main__":
    speak("Initializing Jarvis..... ")

    while True:
        print("Recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening.... ")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)

            word = recognizer.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Yes sir")

                with sr.Microphone() as source:
                    print("Jarvis Activate... ")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error: {0}".format(e))
