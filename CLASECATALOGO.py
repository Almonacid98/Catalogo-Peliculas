from CLASSPELICULAS import *
class Catalogo():
    __catalogolist = []



    def setcatalogo(self, lista):
        self.__catalogolist = lista


    def getcatalogo(self):
        return self.__catalogolist

    def getverPeliculas(self):
        for a in self.__catalogolist:
            print("\nNombre:", a.getnombredepelicula(),
                  "\n Género:", a.gettipodepelicula(), "\n Restricción:", a.getrestriccionesdeedad(),
                  "\n Duración:", a.getduraciondepelicula())

    #def crearPelicula(self):


    def getpopborrarPeliculas(self):
        return self.__catalogolist.pop()

