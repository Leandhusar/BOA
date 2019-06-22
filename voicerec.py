import speech_recognition as sr

def speak():
    record = sr.Recognizer()

    #Entrada de audio del usuario
    with sr.Microphone() as source:
        #Agregar un bloque de codigo para pedir al usuario que hable
        #Despues de la lectura en audio, agregar codigo que confirma la entrada
        print('¿Qué desea hacer?')
        audio = record.listen(source)
        print('Correcto')

    try:
        #Luego de transformar, agregar codigo que confirme la entrada
        entrada = record.recognize_google(audio, language = 'es-SP')
    except:
        entrada = 'Error de reconocimiento'
    
    return entrada

#Prueba
texto = speak()
print(texto)