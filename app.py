from voicerec import speak
from voiceprocessing import *
from online import *
from random import choice
from tkinter import *

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
    seleccion_aleatoria.append([componentes[0],componentes[1]])

    if componentes[0] == None or componentes[1] == None:
        valores = choice(seleccion_aleatoria)
        BAF(valores[0], valores[1])
    #Verificar si se va a ver imagenes
    elif acciones[componentes[0]] == 1 and objetivos[componentes[1]] == 1:
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
    elif acciones[componentes[0]] == 5 or objetivos[componentes[1]] == 7:
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
    componentes = filtrarSolicitud(texto)
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
    if val_accion == 1 and val_objetivo == 1:
        buscarImagen()
    #Verificar si se va a ver un video
    elif val_accion == 1 and val_objetivo == 2:
        buscarVideo()
    #verificar si se buscaran libros
    elif (val_accion == 1 and val_objetivo == 4 or 
        val_accion == 3 and val_objetivo == 4):
        buscarLibro()
    #Verificar so
    elif val_accion == 2 and val_objetivo == 3:
        buscarMusica()
    elif (val_accion == 1 and val_objetivo == 5 or 
        val_accion == 3 and val_objetivo == 5):
        buscarArticulo()
    elif val_accion == 5 and val_objetivo == 7:
        buscarJuego()
    else:
        buscarNoticia()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def ayuda():
    print('este es el boton de ayuda')
    vayuda = Tk()
    vayuda.config(bg = '#505050')
    
    texto = 'Bienvenido a BOA \n \n Si quieres hacer algo pero no sabes qué, presiona el "botón aburrido" \n \n Si quieres hacer algo concreto presiona el boton "¿En qué te puedo ayudar?" \n'
    label = Label(vayuda, text = texto)
    acs = str(seleccion_aleatoria)
    labelacs = Label(vayuda, text = acs)
    label.config(bg = '#505050', fg = '#ffffff')
    labelacs.config(bg = '#505050', fg = '#ffffff')
    label.pack()
    labelacs.pack()


#GUI
ventana = Tk()
ventana.config(bg = '#5f5f5f')
ventana.geometry('150x210')
ventana.resizable(width = False, height = False)

icono = PhotoImage(file = "imagen.png")

# Enlezamos la función a la acción del botón
bayuda = Button(ventana, command = ayuda)
baburrido = Button(ventana, text = "Botón aburrido", command = botonAburrido)
bconcreto = Button(ventana, text = "¿En qué puedo ayudarte?", command = botonConcreto)

bayuda.config(image = icono)
baburrido.config(bg = '#60b0f4', width = 30)
bconcreto.config(bg = '#60b0f4', width = 30, height = 30)


#image = PhotoImage(file = "imagen.png")
#label = Label(image = image)
#label.pack()

bayuda.pack()
baburrido.pack()
bconcreto.pack()

ventana.mainloop()
