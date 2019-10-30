import sys
from CLASSPELICULAS import Peliculas
class Menu():
        def selectmenu(self, nombredepelicula, tipodepelicula, restriccionesdeedad):
            self.__peliculas = Peliculas(nombredepelicula, tipodepelicula, restriccionesdeedad)
            print("BIENVENIDOS AL CATALOGO DE PELICULAS!!! DONDE SIEMPRE SE INFORMA SOBRE CADA PELICULA QUE SALE A CARTELERAS! ")
            print("1 = VER CATALOGO DE PELICULAS DISPONIBLES")
            print("2 = VER PELICULAS CLASIFICADAS SEGUN TIPO DE GENERO")
            print("3 = ELECCION DE PELICULAS SEGUN RESTRICCION DE EDAD")


            #LEER OPCION DE USUARIO
            choice = input("PRESIONE LAS SIGUIENTES OPCIONES PARA PODER EMPEZAR[1/2/3]  = ")

            if choice == "1":
                print(self.__peliculas.nombredepelicula())



