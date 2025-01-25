import pyttsx3

engine = pyttsx3.init()

text = "Hello World!"
engine.say(text)
engine.runAndWait()
