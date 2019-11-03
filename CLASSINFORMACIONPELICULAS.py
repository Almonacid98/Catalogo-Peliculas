class Sinopsis():
    __sinopsis = ''

    def setsinopsis(self, sinopsis):
        self.__sinopsis = sinopsis


    def getsinopsis(self):
        for linea in informacion.archivo.readlines():
            print(linea)
            informacion.archivo.close()
def menusinopsis():
    choice = input("¿DESEA VER SINOPSIS DE ALGUNA PELICULA? [si/no]")
    while True:
        if choice == 'si':
            informacion.archivo = input("Ingrese el nombre de la pelicula:")
            informacion.archivo = open(informacion.archivo, 'r')
            informacion.getsinopsis()
            while True:
                volver = input("¿Desea volver al menu principal?[si/no]:")

                if volver == 'si':
                        print("Volviendo al menu principal....")
                        break

                else:
                        menusinopsis()
            break
        else:
            break
informacion = Sinopsis()








