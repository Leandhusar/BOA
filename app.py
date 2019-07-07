from voicerec import speak
from voiceprocessing import *
from online import *

"""
texto = speak()
print(texto)
"""

"""
accion [0]
objeto [1]
print(filtrarSolicitud('boa quiero leer cincuenta sombras de gray'))
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
