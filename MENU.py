from CLASECATALOGO import *
from CLASSPELICULAS import *
from CLASSDIRECTORES import *
def menuinicio():
    while True:
            print(
                "¡CATALOGO DE PELICULAS!  " "\n ¡BIENVENIDOS! AQUI SE PODRA INFORMAR SOBRE PELICULAS, PARA ELEGIR O RECOMENDAR A OTROS USUARIOS")
            print("1 = VER CATALOGO DE PELICULAS DISPONIBLES")
            print("2 = VER INFORMACION DE DIRECTORES")
            print("3 = BORRAR PELICULAS")
            print("4 = AGREGAR UNA PELICULA A LA LISTA")
            print("5 = EXIT")
            choice = input("PRESIONE LAS SIGUIENTES OPCIONES PARA PODER EMPEZAR[1/2/3/4]  = ")
            if choice == '1':
                catalogos.getcatalogo()
                catalogos.getverPeliculas()
                while True:
                    choice = input("¿DESEA VER SINOPSIS DE ALGUNA PELICULA? [si/no]")
                    if choice == 'si':
                        print("Ingrese el nombre de la pelicula:")
                    elif choice == 'no':
                        print("Volviendo al menu principal........")
                        break
                    else:
                        print("LA OPCION INGRESADA NO ES VALIDA..... INGRESE DE NUEVO UNA OPCION QUE INDIQUE EL MENU")

            elif choice == '2':
                pass
            elif choice == '3':
                catalogos.popborrarPeliculadelista()
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
menuinicio()