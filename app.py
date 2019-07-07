from voicerec import speak
from voiceprocessing import *
from online import *

"""
texto = speak()
print(texto)
"""

#Agregar botones de entrada para solicitudes generales
#funcionalidad de el BOTON ABURRIDO
#... ... ...
def botonAburrido():
    texto = speak()
    componentes = identificar(texto)
    print(componentes)

    #Verificar si se va a ver un video
    if acciones[componentes[0]] == 1 and objetivos[componentes[1]] == 1:
        buscarImagen()
    elif acciones[componentes[0]] == 1 and objetivos[componentes[1]] == 2:
        buscarVideo()
    elif (acciones[componentes[0]] == 1 and objetivos[componentes[1]] == 4 or 
        acciones[componentes[0]] == 3 and objetivos[componentes[1]] == 4):
        buscarLibro()
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
        BAF()

def botonConcreto():
    texto = speak()
    componentes = identificar(texto)
    print(componentes)

    #Busqueda de imagen
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


botonAburrido()
