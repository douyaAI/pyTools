import pyttsx3
import random


def speak(content):

# content = "How would you get undergraduates excited about the field of X?"
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[7].id)
    engine.setProperty('voice', voices[17].id)
    engine.setProperty('voice', voices[26].id)
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('voice', voices[10].id)
    engine.setProperty('voice', voices[29].id)
    engine.say(content)
    # pyttsx3.speak("I will speak this text")
    # engine.say('The quick brown fox jumped over the lazy dog.')
    engine.runAndWait()
    engine.stop()
