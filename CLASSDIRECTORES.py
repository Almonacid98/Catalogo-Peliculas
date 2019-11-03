class Directores():
    def __init__(self, namedirector, peliculaquerealizo, edad, cantidaddepeliculas, anioosdeexperiencia):
        self.__nombredirector = namedirector
        self.__peliculaquerealizo = peliculaquerealizo
        self.__edad = edad
        self.__cantidaddepeliculas = cantidaddepeliculas
        self.__anioosdeexperiecias = anioosdeexperiencia

    def setnombredirector(self, nombre):
        self.__nombredirector = nombre

    def setpeliculashechas(self, quehizo):
        self.__peliculaquerealizo = quehizo

    def setedad(self, edad):
        self.__edad = edad

    def setpeliculascantidad(self, cantidad):
        self.__cantidaddepeliculas = cantidad

    def setexperiencia(self, experiencia):
        self.____anioosdeexperiecias = experiencia

    def getnombredirector(self):
        return self.__nombredirector

    def getpeliculashechas(self):
        return self.__peliculaquerealizo

    def getedad(self):
        return self.__edad

    def getpeliculascantidad(self):
        return self.__cantidaddepeliculas

    def getexperiencia(self):
        return self.__anioosdeexperiecias





