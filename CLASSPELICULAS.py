from CLASSDIRECTORES import *
class Peliculas():
    __nombredepelicula = ''
    __tipodepelicula = ''
    __restriccionesdeedad = ''
    __duracion = ''

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

    def menu2(self):
        while True:
            print("1. SINOPSIS = AVENGERS")
            print("4 = EXIT")
            choice = input("PARA VER SINOPSIS ELIJA OPCION CORRECTA  = ")
            if choice == '1':
               pass
            elif choice == '4':
                print(
                    "GRACIAS POR UTILIZAR NUESTRO SERVICIO.... ESPERAMOS QUE SE HAYA PODIDO INFORMAR... HASTA LA PRÓXIMA!!")
                break
            else:
                print("\n OPCION INCORRECTA.... VUELVA A ELEGIR UNA OPCION EXISTENTE EN EL SISTEMA....")

play = Peliculas("Avengers", "Ciencia ficción", "Apta para mayores de 13 años", "1hs")
