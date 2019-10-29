from CLASSDIRECTORES import *
class Peliculas():
    nombredepelicula = ''
    tipodepelicula = ''
    restriccionesdeedad = ''
    quienhizolapelicula = Directores()

    def __init__(self, nombredepelicula, tipodepelicula, restriccionesdeedad):
        self.__nombredepelicula = nombredepelicula
        self.__tipodepeliculas = tipodepelicula
        self.__restriccionesdeedad = restriccionesdeedad

    def getnombredepelicula(self):
        return print(self.__nombredepelicula)

    def gettipodepelicula(self):
        return print(self.__tipodepeliculas)

    def getrestriccionesdeedad(self):
        return print(self.__restriccionesdeedad)


print("Bienvenidos a la cartelera de información de cine")
play = Peliculas("Avengers", "Ciencia ficción", "Apta para mayores de 13 años")
play.getnombredepelicula()
play.gettipodepelicula()
play.getrestriccionesdeedad()
