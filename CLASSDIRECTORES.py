class Directores():
    __nombrededirector = ''
    __pelicularealizada = ''
    __edad = ''
    __cantidaddepelicualas = ''
    __aniosdeexperiencia = ''

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