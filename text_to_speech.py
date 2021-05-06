import pyttsx3

#text to speech
def speak(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 125)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()