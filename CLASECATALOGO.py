from CLASSPELICULAS import *
from CLASSDIRECTORES import *
class Catalogo():
    __catalogolist = []
    __Directoreslist = []


    def setcatalogo(self, lista):
        self.__catalogolist = lista



    def setdirectores(self, directores):
        self.__Directoreslist = directores



    def agregarPelicula(self):
        nombredepelicula = input("INGRESE EL NOMBRE DE LA PELICULA QUE DESEA AGREGAR A LA LISTA =")
        tipodepelicula = input("INGRESE QUE TIPO DE PELICULA ES =")
        restriccionesdeedad = input("INGRESE LA RESTRICCION DE EDAD = ")
        duracion = input("INGRESE EL TIEMPO ESTIMADO DE DURACION DE LA PELICULA A CREAR = ")
        pelicula = Peliculas(nombredepelicula, tipodepelicula, restriccionesdeedad, duracion)
        self.__catalogolist.append(pelicula)


    def borrarPeliculadelista(self):
        self.getverPeliculas()
        self.__catalogolist.remove(input("Ingrese la pelicula que desea eliminar:"))


    def getverPeliculas(self):
        for a in self.__catalogolist:
            print("\nNombre:", a.getnombredepelicula(),
                  "\n Género:", a.gettipodepelicula(), "\n Restricción:", a.getrestriccionesdeedad(),
                  "\n Duración:", a.getduraciondepelicula())


    def getverdirectores(self):
        for a in self.__Directoreslist:
            print("\nNombre del director:", a.getnombredirector(),
                  "\n Pelicula que realizó:", a.getpeliculashechas(), "\n Edad:", a.getedad(),
                  "\n Cantidad de peliculas:", a.getpeliculascantidad(), "\n Años de experiencia:", a.getexperiencia())


    def getcatalogo(self):
        return self.__catalogolist


    def getdirectores(self):
        return self.__Directoreslist