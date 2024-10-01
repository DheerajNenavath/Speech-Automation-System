import speech_recognition as sr
import webbrowser
import subprocess
import os

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("Listening...")
        audio = recognizer.listen(source)

        try:
            print("Recognizing speech...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")

            # Open browser if the command is recognized
            if "open browser" in text.lower():
                print("Opening browser...")
                webbrowser.open("http://www.google.com")

            # Open a specific application if the command is recognized
            elif "open calculator" in text.lower():
                print("Opening calculator...")
                # For Windows, use subprocess to open Calculator
                subprocess.Popen("calc.exe")

            elif "open notepad" in text.lower():
                print("Opening Notepad...")
                # For Windows, use subprocess to open Notepad
                subprocess.Popen("notepad.exe")

            elif "open vscode" in text.lower() or "open visual studio code" in text.lower():
                print("Opening Visual Studio Code...")
                # Use the correct path for your system
                subprocess.Popen([r"C:\path\to\your\code.exe"])

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from the service; {e}")

if __name__ == "__main__":
    recognize_speech()


