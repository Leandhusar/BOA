#Este diccionario almacena acciones o verbos
acciones = {'mirar':1, 'ver':1, 'escuchar':2, 'jugar':3, 'oir':2}

#Este diccionario almacena objetos o sujetos
objetos = {'imagen':1, 'video':2, 'musica':3, 'juego':4, 'cancion':3}

verbo = tuple(acciones.keys())
objetivo = tuple(objetos.keys())

def solicitado(entrada):
    if entrada.find('boa') >= 0:
        return True
    else: 
        return False

def identificar(texto):
    if solicitado(texto):
        accion = buscarAcciones(texto)
        objeto = buscarObjetos(texto)
    else: pass
    print('Accion:', accion)
    print('objeto:', objeto)

def buscarAcciones(entrada):
    #Buscar acción dentro de las palabras que dice el usuario
    for e in verbo:
      if (e in entrada):
        # entrada: escuchar música 
        # verbo: escuchar
        return e

def buscarObjetos(entrada):
    #Buscar acción dentro de las palabras que dice el usuario
    for e in objetivo:
      if (e in entrada):
        # entrada: escuchar música 
        # verbo: escuchar
        return e

identificar("boa, quiero ver un video")
identificar("boa, escuchar una cancion")