import speech_recognition as sr
import webbrowser

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

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from the service; {e}")

if __name__ == "__main__":
    recognize_speech()

