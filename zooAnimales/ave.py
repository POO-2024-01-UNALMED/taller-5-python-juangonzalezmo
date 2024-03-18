from animal import Animal

class Ave (Animal):
    _listado = []
    halcones = 0
    aguilas = 0
    def __init__(self, nombre="", edad=0, habitat="", genero="", colorPlumas=""):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)

    @classmethod
    def setListado(cls,listado):
        cls._listado = listado
    @classmethod
    def getListado(cls):
        return cls._listado
    def setColorPlumas(self,color):
        self._colorPlumas = color
    def getColorPlumas(self):
        return self._colorPlumas
    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)
    @staticmethod
    def movimiento():
        cadena = "volar"
        return cadena
    @classmethod
    def crearHalcon(cls,nombre, edad, genero):
        ave = Ave(nombre,edad,"montanas",genero,"cafe glorioso")
        cls.halcones+=1
        return ave
    @classmethod
    def crearAguila(cls,nombre, edad, genero):
        ave = Ave(nombre,edad,"montanas",genero,"blanco y amarillo")
        cls.aguilas+=1
        return ave