import speech_recognition as sr

def listen_command():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        our_speech = r.recognize_google(audio, language="ru")
        return our_speech
    except Exception as ex:
        print(ex)
