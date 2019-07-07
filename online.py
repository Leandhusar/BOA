from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Controlador del navegador
#navegador = webdriver.Chrome('chromedriver')
#navegador.get('https://www.google.com/')

#searchbar = navegador.find_element_by_class_name('gLFyf.gsfi')
#searchbar.send_keys('perritos')
#searchbar.send_keys(Keys.ENTER)

#buscar videos especificados
def videoConcreto(titulo):
    lista = titulo.split(' ')
    busqueda = "+".join(lista)
    navegador = webdriver.Chrome('chromedriver')
    navegador.maximize_window()
    pagina = 'https://www.youtube.com/results?search_query=' + busqueda
    navegador.get(pagina)

#Buscar imagenes especificadas
def imagenConcreta(titulo):
    lista = titulo.split(' ')
    busqueda = "+".join(lista)
    navegador = webdriver.Chrome('chromedriver')
    pagina = "https://www.google.com.co/search?hl=es&biw=1920&bih=969&tbm=isch&sa=1&ei=PdsfXbeRK-jV5gLE4J3IAQ&q={}&oq={}&gs_l=img.3..0l10.11707.15294..16867...4.0..0.452.2320.0j3j3j2j1......0....1..gws-wiz-img.......0i67j0i8i30j0i24.M7xijxAd1Ag".format(busqueda,  busqueda)
    navegador.get(pagina)

#Buscar libros especificados
def libroConcreto(titulo):
    lista = titulo.split(' ')
    busqueda = "+".join(lista)
    navegador = webdriver.Chrome('chromedriver')
    pagina = "https://www.google.com/search?tbm=bks&q=" + busqueda
    navegador.get(pagina)

#Buscar cancion especificada
def cancionConcreta(titulo):
    lista = titulo.split(' ')
    busqueda = "%20".join(lista)
    navegador = webdriver.Chrome('chromedriver')
    pagina = "https://soundcloud.com/search?q=" + busqueda
    navegador.get(pagina)

#consulta o busqueda concreta
def busquedaConcreta(titulo):
    lista = titulo.split(' ')
    busqueda = "+".join(lista)
    navegador = webdriver.Chrome('chromedriver')
    pagina = "https://www.google.com/search?q={}&oq={}&aqs=chrome..69i57.2029j0j8&sourceid=chrome&ie=UTF-8".format(busqueda, busqueda)
    navegador.get(pagina)

#Busca un juego en concreto en Steam
def juegoConcreto(titulo):
    lista = titulo.split(' ')
    busqueda = "+".join(lista)
    navegador = webdriver.Chrome('chromedriver')
    pagina = "https://store.steampowered.com/search/?term=" + busqueda
    navegador.get(pagina)

#Se realizan búsquedas que quedan a disposicion del usuario -> No definidas

def buscarImagen():
    navegador = webdriver.Chrome('chromedriver')
    pagina = "https://wallhaven.cc/random?page=2"
    navegador.get(pagina)

def buscarVideo():
    navegador = webdriver.Chrome('chromedriver')
    pagina = "https://www.youtube.com"
    navegador.get(pagina)

def buscarMusica():
    navegador = webdriver.Chrome('chromedriver')
    pagina = "https://soundcloud.com"
    navegador.get(pagina)

def buscarLibro():
    navegador = webdriver.Chrome('chromedriver')
    pagina = "https://www.amazon.es/comprar-libros-español/b?ie=UTF8&node=599364031"
    navegador.get(pagina)

def buscarJuego():
    navegador = webdriver.Chrome('chromedriver')
    pagina = "https://store.steampowered.com"
    navegador.get(pagina)

def buscarArticulo():
    navegador = webdriver.Chrome('chromedriver')
    pagina = "https://es.wikipedia.org/wiki/Wikipedia:Portada"
    navegador.get(pagina)

def buscarNoticia():
    navegador = webdriver.Chrome('chromedriver')
    pagina = "https://news.google.com/?hl=es-419&gl=CO&ceid=CO:es-419"
    navegador.get(pagina)
