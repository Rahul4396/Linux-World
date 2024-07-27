pip install pyttsx3


import pyttsx3

def speak_text(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()
    
    # Set properties before adding anything to speak
    engine.setProperty('rate', 150)  # Speed percent (can go over 100)
    engine.setProperty('volume', 0.9)  # Volume 0-1
    
    # Queue the text to be spoken
    engine.say(text)
    
    # Flush the say() queue and play the audio
    engine.runAndWait()

if __name__ == "__main__":
    text = input("Enter the text you want to convert to speech: ")
    speak_text(text)
