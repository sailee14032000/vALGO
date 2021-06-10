import pyttsx3

class voice_assistant(object):
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('volume',1.0)
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice',self.voices[1].id)
    def speak(self,sentence):
        sentence = sentence.strip()
        self.engine.say(sentence)
        self.engine.runAndWait()
        self.engine.stop()

