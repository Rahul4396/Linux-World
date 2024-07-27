pip install SpeechRecognition pyaudio


import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Capture speech and convert to text
with sr.Microphone() as source:
    print("Say something:")
    audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError:
        print("Could not request results; check your network connection")
