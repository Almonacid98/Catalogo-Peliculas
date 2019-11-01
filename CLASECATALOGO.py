from CLASSDIRECTORES import *
from CLASSPELICULAS import *
class Catalogo():
    catalogo = []
    def verPeliculas(self, catalogo):
        for a in catalogo:
            print("\nNombre:", a.getnombredepelicula(),
                  "\n Tipo:", a.gettipodepelicula(), "\n Restricción:", a.getrestriccionesdeedad(),
                  "\n Duración:", a.getduraciondepelicula)

    def crearPelicula(self):
        pelis = Peliculas()
        self.catalogo.append(pelis)

    def popborrarPeliculas(self):
        return self.catalogo.pop()

    def menu(self):
        while True:
            print(
                "¡CATALOGO DE PELICULAS!  " "\n ¡BIENVENIDOS! AQUI SE PODRA INFORMAR SOBRE PELICULAS, PARA ELEGIR O RECOMENDAR A OTROS USUARIOS")
            print("1 = VER CATALOGO DE PELICULAS DISPONIBLES")
            print("2 = AGREGAR PELICULAS")
            print("3 = BORRAR PELICULAS")
            print("4 = EXIT")
            choice = input("PRESIONE LAS SIGUIENTES OPCIONES PARA PODER EMPEZAR[1/2/3]  = ")
            if choice == '1':
                catalogos.verPeliculas()
            elif choice == '2':
                catalogos.crearPelicula()
            elif choice == '3':
                catalogos.popborrarPeliculas()
            elif choice == '4':
                print(
                    "GRACIAS POR UTILIZAR NUESTRO SERVICIO.... ESPERAMOS QUE SE HAYA PODIDO INFORMAR... HASTA LA PRÓXIMA!!")
                break
            else:
                print("\n OPCION INCORRECTA.... VUELVA A ELEGIR UNA OPCION EXISTENTE EN EL SISTEMA....")

catalogos = Catalogo()
catalogos.menu()
