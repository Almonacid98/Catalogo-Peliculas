from CLASSPELICULAS import *
class Catalogo():
    catalogolist = []
    def verPeliculas(self):
        for a in self.catalogolist:
            print("\nNombre:", a.getnombredepelicula(),
                  "\n Género:", a.gettipodepelicula(), "\n Restricción:", a.getrestriccionesdeedad(),
                  "\n Duración:", a.getduraciondepelicula())

    def crearPelicula(self):
        pelis = Peliculas("The Avengers: Los Vengadores", "Acción | Aventura | Ciencia ficción", "Apta para mayores de 12", "2h 23m")
        pelis1 = Peliculas("Deadpool", "Acción | Aventura | Comedia", "Apta para mayores de 18", "1h 49m")
        #pelis2 = Peliculas()
        self.catalogolist.append(pelis)
        self.catalogolist.append(pelis1)
        #self.catalogolist.append(pelis2)

    def popborrarPeliculas(self):
        return self.catalogolist.pop()

    def menuinicio(self):
        while True:
            print(
                "¡CATALOGO DE PELICULAS!  " "\n ¡BIENVENIDOS! AQUI SE PODRA INFORMAR SOBRE PELICULAS, PARA ELEGIR O RECOMENDAR A OTROS USUARIOS")
            print("1 = VER CATALOGO DE PELICULAS DISPONIBLES")
            print("2 = VER INFORMACION DE DIRECTORES")
            print("3 = BORRAR PELICULAS")
            print("4 = EXIT")
            choice = input("PRESIONE LAS SIGUIENTES OPCIONES PARA PODER EMPEZAR[1/2/3/4]  = ")
            if choice == '1':
                catalogos.crearPelicula()
                catalogos.verPeliculas()
                while True:
                    choice = input("¿DESEA VER SINOPSIS DE ALGUNA PELICULA? [si/no]")
                    if choice == 'si':
                        print("Ingrese el nombre de la pelicula:")

                    else:
                        print("El nombre de la pelicula no es válido, o no existe en nuestra lista de catalogos")

            elif choice == '2':
                pass
            elif choice == '3':
                catalogos.popborrarPeliculas()
            elif choice == '4':
                print(
                    "GRACIAS POR UTILIZAR NUESTRO SERVICIO.... ESPERAMOS QUE SE HA1YA PODIDO INFORMAR... HASTA LA PRÓXIMA!!")
                break
            else:
                print("\n OPCION INCORRECTA.... VUELVA A ELEGIR UNA OPCION EXISTENTE EN EL SISTEMA....")

catalogos = Catalogo()
catalogos.menuinicio()
