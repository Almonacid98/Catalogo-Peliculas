from CLASECATALOGO import *
from CLASSPELICULAS import *
from CLASSDIRECTORES import *
from CLASSINFORMACIONPELICULAS import *
def menuinicio():
    while True:
            print(
                "¡CATALOGO DE PELICULAS!  " "\n ¡BIENVENIDOS! AQUI SE PODRA INFORMAR SOBRE PELICULAS, PARA ELEGIR O RECOMENDAR A OTROS USUARIOS")
            print("1 = VER CATALOGO DE PELICULAS DISPONIBLES")
            print("2 = VER INFORMACION DE DIRECTORES")
            print("3 = BORRAR PELICULAS")
            print("4 = AGREGAR UNA PELICULA A LA LISTA")
            print("5 = EXIT")
            choice = input("PRESIONE LAS SIGUIENTES OPCIONES PARA PODER EMPEZAR[1/2/3/4/5]  = ")
            if choice == '1':
                catalogos.getcatalogo()
                catalogos.getverPeliculas()
                menusinopsis()

            elif choice == '2':
                catalogos.getdirectores()
                catalogos.getverdirectores()

            elif choice == '3':
                catalogos.borrarPeliculadelista()

            elif choice == '4':
                catalogos.agregarPelicula()

            elif choice == '5':
                print(
                    "GRACIAS POR UTILIZAR NUESTRO SERVICIO.... ESPERAMOS QUE SE HA1YA PODIDO INFORMAR... HASTA LA PRÓXIMA!!")
                break
            else:
                print("\n OPCION INCORRECTA.... VUELVA A ELEGIR UNA OPCION EXISTENTE EN EL SISTEMA....")



catalogos = Catalogo()
pelis = Peliculas("The Avengers: Los Vengadores", "Acción | Aventura | Ciencia ficción", "Apta para mayores de 12", "2h 23m")
pelis1 = Peliculas("Deadpool", "Acción | Aventura | Comedia", "Apta para mayores de 18", "1h 49m")
pelis2 = Peliculas("Rápido y furioso", " Acción | Crimen | Suspenso", "Apta para mayores de 15 años", "1h 47m")
catalogos.getcatalogo().append(pelis)
catalogos.getcatalogo().append(pelis1)
catalogos.getcatalogo().append(pelis2)
director = Directores("Anthony Russo y Joe Russo", "Pieces, Welcome to Collinwood, Capitán América: Civil War, Avengers: Endgame",
                      "Anthony:49 y Joe:48 años", "Contienen aproximadamente 30 peliculas realizadas", "Contienen acerca de mas de 23 años de experiencia como directores")
catalogos.getdirectores().append(director)
menuinicio()