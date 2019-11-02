from CLASSPELICULAS import *
from CLASSDIRECTORES import *
class Catalogo():
    __catalogolist = []
    __Directoreslist = []


    def setcatalogo(self, lista):
        self.__catalogolist = lista


    def getcatalogo(self):
        return self.__catalogolist



    def agregarPelicula(self):
        nombredepelicula = input("INGRESE EL NOMBRE DE LA PELICULA QUE DESEA AGREGAR A LA LISTA =")
        tipodepelicula = input("INGRESE QUE TIPO DE PELICULA ES =")
        restriccionesdeedad = input("INGRESE LA RESTRICCION DE EDAD = ")
        duracion = input("INGRESE EL TIEMPO ESTIMADO DE DURACION DE LA PELICULA A CREAR = ")
        pelicula = Peliculas(nombredepelicula, tipodepelicula, restriccionesdeedad, duracion)
        self.__catalogolist.append(pelicula)


    def popborrarPeliculadelista(self):
        self.getverPeliculas()
        borrar = input("INGRESE EL NOMBRE DE LA PELICULA QUE DESEA BORRAR DE LA LISTA = ")
        print("BORRANDO DATOS.......")
        self.__catalogolist.pop(borrar)
    def getverPeliculas(self):
        for a in self.__catalogolist:
            print("\nNombre:", a.getnombredepelicula(),
                  "\n Género:", a.gettipodepelicula(), "\n Restricción:", a.getrestriccionesdeedad(),
                  "\n Duración:", a.getduraciondepelicula())

    def getverdirectores(self):
        for a in self.__catalogolist:
            print("\nNombre del director:", a.getnombredepelicula(),
                  "\n Pelicula que realizó:", a.gettipodepelicula(), "\n Edad:", a.getrestriccionesdeedad(),
                  "\n Cantidad de peliculas:", a.getduraciondepelicula(), "\n Años de experiencia:")



    def getpopborrarPeliculas(self):
        return self.__catalogolist.pop()

