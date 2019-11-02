
class Sinopsis():
    __sinopsis = ''

    def setsinopsis(self, sinopsis):
        self.__sinopsis = sinopsis


    def getsinopsis(self):
        for linea in informacion.archivo.readlines():
            print(linea)
            informacion.archivo.close()





informacion = Sinopsis()
informacion.archivo = open("Sinopsis Avengers.txt", 'r')
