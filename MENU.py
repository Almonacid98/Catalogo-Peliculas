import sys
from CLASSPELICULAS import Peliculas
class Menu():
    #Creacion de menu mediante un constructor
    def __init__(self):
        self.__peliculas = Peliculas()
        self.__selection = {
                            "1": self.__peliculas.getnombredepelicula(),
                            "2": self.__peliculas.gettipodepelicula(),
                            "3": self.__peliculas.getrestriccionesdeedad()
        }

    def vermenu(self):
        print(""""
     BIENVENIDOS AL CATALOGO DE PELICULAS!!! DONDE SIEMPRE SE INFORMA SOBRE CADA PELICULA QUE SALE A CARTELERAS!
     PRESIONE LAS SIGUIENTES OPCIONES PARA PODER EMPEZAR:
     1 = CATALOGO DE INFORMACION DE PELICULAS DISPONIBLES
     2 = PELICULAS POR EL TIPO DE GENERO QUE LE GUSTEN 
     3 = ELECCION DE PELICULAS SEGUN RESTRICCIONES DE EDAD
     
        
  
        """)

    def ejecuciondemenu(self):
        #muestra el menu y responde a lo que la persona requiere
        while True:
            self.vermenu()
            seleccionaropcion = input("INGRESA UNA OPCION PARA COMENZAR: ")
            accionseleccion = self.__selection.get(seleccionaropcion)
            if accionseleccion:
                accionseleccion()
            else:
                print("LA OPCION INGRESADA NO ES UNA OPCION VALIDA".format(seleccionaropcion))
    def mostrarinformacion(self, nombre = None):
        if not nombre:
             nombre = self.__peliculas.getnombredepelicula()
        for nombrepelicula in nombre:
            print("[0]: [1]\n[2]".format(nombrepelicula))
