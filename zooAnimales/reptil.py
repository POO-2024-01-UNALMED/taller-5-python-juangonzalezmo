from .animal import Animal

class Reptil(Animal):
    _listado = []
    iguanas = 0
    serpientes = 0
    def __init__(self, nombre="", edad=0, habitat="", genero="", colorEscamas="", largoCola=0):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)

    @classmethod
    def setListado(cls,listado):
        cls._listado = listado
    @classmethod
    def getListado(cls):
        return cls._listado
    def setColorEscamas(self,color):
        self._colorEscamas = color
    def getColorEscamas(self):
        return self._colorEscamas
    def setLargoCola(self,largo):
        self._largoCola = largo
    def getLargoCola(self):
        return self._largoCola
    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)
    @staticmethod
    def movimiento():
        cadena = "reptar"
        return cadena
    @classmethod
    def crearIguana(cls,nombre, edad, genero):
        reptil = Reptil(nombre,edad,"humedal",genero,"verde",3)
        cls.iguanas+=1
        return reptil
    @classmethod
    def crearSerpiente(cls,nombre, edad, genero):
        reptil = Reptil(nombre,edad,"jungla",genero,"blanco",1)
        cls.serpientes+=1
        return reptil
