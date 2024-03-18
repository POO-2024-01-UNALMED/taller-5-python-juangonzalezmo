from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0
    def __init__(self, nombre="", edad=0, habitat="", genero="", colorPiel="", venenoso=False):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    @classmethod
    def setListado(cls,listado):
        cls._listado = listado
    @classmethod
    def getListado(cls):
        return cls._listado
    def setColorPiel(self,color):
        self._colorPiel = color
    def getColorPiel(self):
        return self._colorPiel
    def setVenenoso(self,venenoso):
        self._venenoso = venenoso
    def getVenenoso(self):
        return self._venenoso
    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)
    @staticmethod
    def movimiento():
        cadena = "saltar"
        return cadena
    @classmethod
    def crearRana(cls,nombre, edad, genero):
        anfibio = Anfibio(nombre,edad,"selva",genero,"rojo",True)
        cls.ranas+=1
        return anfibio
    @classmethod
    def crearSalamandra(cls,nombre, edad, genero):
        anfibio = Anfibio(nombre,edad,"selva",genero,"negro y amarillo",False)
        cls.salamandras+=1
        return anfibio
