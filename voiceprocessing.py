#Contiene las acciones del usuario
acciones = {
    'mirar':1, 'ver':1, 'observar':1, 'escuchar':2, 
    'oir': 2, 'leer':3, 'saber':4, 'consultar':4, 'jugar':5
}

#Contiene los objetivos del usuario
objetivos = {
    'imagen':1, 'foto':1, 'pintura':1, 'video':2, 'música':3, 
    'canción':3, 'libro':4, 'artículo':5, 'noticia':6, 'juego':7
}

#Estado inicial de la basua -> Elementos que no deben ser tomados en 
#cuenta para realizar las búsquedas
basura = ['Oye', 'quiero']
accion = tuple(acciones.keys())
objetivo = tuple(objetivos.keys())

for a in accion:
    basura.append(a)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#Se realizará el procesamiento de la solicitud realizada por el
#usuario solo si se invoca con 'boa'
#Se retorna True si existe una solicitud del usuario
def solicitado(entreda):
    if entreda.find('Oye') >= 0:
        return True
    return False

#Funcion para identificar la accion y objetivo del usuario
#Retorna una lista con dos elementos:
#prlist = [accion, objetivo]
#SOLO USARLA PARA UNA SOLICITUD GENERAL
def identificar(entrada):
    accion_usuario = ''
    objetivo_usuario = ''

    print(entrada)
    if solicitado(entrada):
        accion_usuario = buscarAccion(entrada)
        objetivo_usuario = buscarObjetivo(entrada)
    return [accion_usuario, objetivo_usuario]

#Filtrado para versiones específicas
#SOLO USAR SI EL USUARIO HA DEFENIDO ALGO EN ESPECIFICO
def filtrarSolicitud(entrada):
    solicitud = entrada.split(' ')
    accion_usuario = ''
    objetivo_usuario = ''

    print(solicitud)
    if solicitado(entrada):
        for palabra in solicitud:
            if palabra == 'Oye':
                solicitud.remove(palabra)
                break
        accion_usuario = buscarAccion(entrada)
        #Eliminar todas las palabras que interfieran con
        #la busqueda. Solo se valida lo que se consiga
        #despues de la accion
        pos = solicitud.index(accion_usuario)
        for palabra in range(pos):
            solicitud.remove(solicitud[palabra])
        solicitud.remove(accion_usuario)
        objetivo_usuario = " ".join(solicitud)
    #Devuelve una lista [accion, objetivo]
    return [accion_usuario, objetivo_usuario]
    

#Buscar la accion del usuario
def buscarAccion(entrada):
    #Buscar dentro de las palabras que dice el usuario
    for a in accion:
        if a in entrada:
            return a

#Buscar el objetivo del usuario
def buscarObjetivo(entrada):
    for o in objetivo:
        if o in entrada:
            return o

#print(identificar('boa quiero ver videos'))
#print(filtrarSolicitud('boa quiero mirar videos de gatitos corriendo'))
