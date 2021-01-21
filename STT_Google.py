# Before you install speech recognition make sure you have pyAudio installed.

import speech_recognition as sr # importing speech recognition api

message = ""

while True:
    r = sr.Recognizer()  # initialize recognizer
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)  # listen to the source
        try:
            message = r.recognize_google(audio)  # use recognizer to convert audio to text
            print("You said : {}".format(message))
        except:
            print("Sorry could not recognize your voice")  # in case of voice not recognized
    if message == "bye" or message == "goodbye": # when the user says "bye" or "goodbye" the program terminates
        break