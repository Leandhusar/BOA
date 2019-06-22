import speech_recognition as sr
from reswords import *

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Di algo")
    audio = r.listen(source)
    print("Procesando...")

try:
    texto = r.recognize_google(audio, language = 'es-SP')
    print("Has dicho: ", texto)
except:
    pass

identificar(texto)
