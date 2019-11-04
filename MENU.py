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
                      "Anthony:49 y Joe:48 años", "Contienen aproximadamente 30 peliculas realizadas", "Contienen acerca de mas de 30 años de experiencia como directores")
director1 = Directores("Tim Miller", "Hideaway(1995) , La chica del dragón tatuado(2011), Thor: The Dark World (2013), Deadpool (2016) ,Terminator: Dark Fate (2019) ","49 años",
                       "Contiene mas de 7 peliculas realizadas", "Contiene acerca de 25 años de experiencia como director" )
director2 = Directores("Justin lin y James Wan", "Saga completa de Rapidos y furiosos", "Justin: 46 y james:42", "Contiene aproximadamente 15 peliculas"
                       , "Contienen más de 15 años de experiencia como directores")
catalogos.getdirectores().append(director)
catalogos.getdirectores().append(director1)
catalogos.getdirectores().append(director2)
menuinicio()