from voicerec import speak
from voiceprocessing import *
from online import *
from random import choice

"""
texto = speak()
print(texto)
"""

seleccion_aleatoria = [[1, 1], [1, 2], [1, 4], [3, 4], [2, 3], [1, 5], [3, 5], [5, 7], [1, 6], [3, 6], [4, 6]]

#Agregar botones de entrada para solicitudes generales
#funcionalidad de el BOTON ABURRIDO
#... ... ...
def botonAburrido():
    texto = speak()
    componentes = identificar(texto)
    print(componentes)

    #Verificar si se va a ver imagenes
    if acciones[componentes[0]] == 1 and objetivos[componentes[1]] == 1:
        buscarImagen()
    #Verificar si se va a ver un video
    elif acciones[componentes[0]] == 1 and objetivos[componentes[1]] == 2:
        buscarVideo()
    #verificar si se buscaran libros
    elif (acciones[componentes[0]] == 1 and objetivos[componentes[1]] == 4 or 
        acciones[componentes[0]] == 3 and objetivos[componentes[1]] == 4):
        buscarLibro()
    #Verificar so
    elif acciones[componentes[0]] == 2 and objetivos[componentes[1]] == 3:
        buscarMusica()
    elif (acciones[componentes[0]] == 1 and objetivos[componentes[1]] == 5 or 
        acciones[componentes[0]] == 3 and objetivos[componentes[1]] == 5):
        buscarArticulo()
    elif acciones[componentes[0]] == 5 and objetivos[componentes[1]] == 7:
        buscarJuego()
    elif (acciones[componentes[0]] == 1 and objetivos[componentes[1]] == 6 or 
        acciones[componentes[0]] == 3 and objetivos[componentes[1]] == 6 or 
        acciones[componentes[0]] == 4 and objetivos[componentes[1]] == 6):
        buscarNoticia()
    else:
        valores = choice(seleccion_aleatoria)
        BAF(valores[0], valores[1])

#Busquedas especificas  
def botonConcreto():
    texto = speak()
    componentes = identificar(texto)
    print(componentes)

    #Las busquedas de imagenes es mas restringida
    if acciones[componentes[0]] == 1 and 'imagen' in componentes[1]:
        imagenConcreta(componentes[1])
    elif acciones[componentes[0]] == 1 or 'video' in componentes[1]:
        videoConcreto(componentes[1])
    elif (acciones[componentes[0]] == 1 and 'libro' in componentes[1] or 
        acciones[componentes[0]] == 3):
        libroConcreto(componentes[1])
    elif acciones[componentes[0]] == 2:
        cancionConcreta(componentes[1])
    elif acciones[componentes[0]] == 4:
        busquedaConcreta(componentes[1])
    elif acciones[componentes[0]] == 5:
        juegoConcreto(componentes[1])
    else:
        print('No entendí')

def BAF(val_accion, val_objetivo):
    #Selecciona las actividades por ... ruleta?
    #Verificar si se va a ver imagenes
    if acciones[val_accion] == 1 and objetivos[val_objetivo] == 1:
        buscarImagen()
    #Verificar si se va a ver un video
    elif acciones[val_accion] == 1 and objetivos[val_objetivo] == 2:
        buscarVideo()
    #verificar si se buscaran libros
    elif (acciones[val_accion] == 1 and objetivos[val_objetivo] == 4 or 
        acciones[val_accion] == 3 and objetivos[val_objetivo] == 4):
        buscarLibro()
    #Verificar so
    elif acciones[val_accion] == 2 and objetivos[val_objetivo] == 3:
        buscarMusica()
    elif (acciones[val_accion] == 1 and objetivos[val_objetivo] == 5 or 
        acciones[val_accion] == 3 and objetivos[val_objetivo] == 5):
        buscarArticulo()
    elif acciones[val_accion] == 5 and objetivos[val_objetivo] == 7:
        buscarJuego()
    else:
        buscarNoticia()

botonAburrido()
