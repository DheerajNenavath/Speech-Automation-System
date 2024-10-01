import speech_recognition as sr

def recognize_speech():
    # Initialize recognizer class (for recognizing speech)
    recognizer = sr.Recognizer()

    # Use the microphone as source for input.
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("Listening...")
        audio = recognizer.listen(source)

        try:
            # Recognize speech using Google Speech Recognition
            print("Recognizing speech...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from the service; {e}")

if __name__ == "__main__":
    recognize_speech()
