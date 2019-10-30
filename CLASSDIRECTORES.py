class Directores():
    nombrededirector = ''
    pelicularealizada = ''
    edad = ''
    cantidaddepelicualas = ''
    añosdeexperiencia = ''

    def __init__(self, namedirector, peliculaquerealizo, edad, cantidaddepeliculas, añosdeexperiencia):
        self.__nombredirector = namedirector
        self.__peliculaquerealizo = peliculaquerealizo
        self.__edad = edad
        self.__cantidaddepeliculas = cantidaddepeliculas
        self.__añosdeexperiecias = añosdeexperiencia

    def setnombredirector(self, nombre):
        self.__nombredirector = nombre

    def setpeliculashechas(self, quehizo):
        self.__peliculaquerealizo = quehizo

    def setedad(self, edad):
        self.__edad = edad