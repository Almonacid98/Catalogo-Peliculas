from CLASSDIRECTORES import *
class Peliculas():
    nombredepelicula = ''
    tipodepelicula = ''
    restriccionesdeedad = ''
    duracion = ''
    quienhizolapelicula = Directores()

    def __init__(self, nombredepelicula, tipodepelicula, restriccionesdeedad, duracion):
        self.__nombredepelicula = nombredepelicula
        self.__tipodepeliculas = tipodepelicula
        self.__restriccionesdeedad = restriccionesdeedad
        self.__duracion = duracion

    def setnombredepelicula(self, nombredepelicula):
        self.__nombredepelicula = nombredepelicula


    def settipodepelicula(self, tipodepeliculas):
        self.__tipodepeliculas = tipodepeliculas


    def setrestriccionesdeedad(self, restriccionesdeedad):
        self.__restriccionesdeedad = restriccionesdeedad


    def setduraciondepelicula(self, duraciondepelicula):
        self.__duracion = duraciondepelicula


    def getnombredepelicula(self):
        return self.__nombredepelicula


    def gettipodepelicula(self):
        return self.__tipodepeliculas


    def getrestriccionesdeedad(self):
        return self.__restriccionesdeedad


    def getduraciondepelicula(self):
        return self.__duracion


play = Peliculas("Avengers", "Ciencia ficción", "Apta para mayores de 13 años")
print(play.getnombredepelicula())
print(play.gettipodepelicula())
print(play.getrestriccionesdeedad())
