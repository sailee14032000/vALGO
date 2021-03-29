
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('volume',1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say("inserting 22 to left")

engine.runAndWait()
