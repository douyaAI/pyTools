import pyttsx3
import random
import sys


def speak(content, isMale):

# content = "How would you get undergraduates excited about the field of X?"
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[10].id)
    engine.setProperty('voice', voices[7].id)
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('voice', voices[17].id)
    engine.setProperty('voice', voices[26].id)

    voice_choice = 0 if isMale== 0 else 17
    engine.setProperty('voice', voices[voice_choice].id)
    engine.say(content)
    # pyttsx3.speak("I will speak this text")
    # engine.say('The quick brown fox jumped over the lazy dog.')
    engine.runAndWait()

if __name__ == "__main__":
    content = "Can you talk a little bit about your current research?"
    isMale = 0
    if len(sys.argv) >= 2:
        content = sys.argv[1]
    if len(sys.argv) >= 3:
        isFemale = int(sys.argv[2])
    speak(content, isFemale)
