from .animal import Animal

class Pez(Animal):
    _listado =[]
    salmones = 0
    bacalaos = 0
    def __init__(self, nombre="", edad=0, habitat="", genero="", colorEscamas = "", cantidadAletas=0):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas= colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)

    @classmethod
    def setListado(cls,listado):
        cls._listado = listado
    @classmethod
    def getListado(cls):
        return cls._listado
    def setColorEscamas(self,colorEscamas):
        self._colorEscamas = colorEscamas
    def getColorEscamas (self):
        return self._colorEscamas
    def setCantidadAletas(self,aletas):
        self._cantidadAletas = aletas
    def getCantidadAletas(self):
        return self._cantidadAletas
    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)
    @staticmethod
    def movimiento():
        cadena= "nadar"
        return cadena
    @classmethod
    def crearSalmon(cls,nombre,edad,genero):
        pez = Pez(nombre, edad ,"oceano", genero, "rojo", 6)
        cls.salmones+=1
        return pez
    @classmethod
    def crearBacalao(cls,nombre,edad,genero):
        pez = Pez(nombre, edad ,"oceano", genero, "gris", 6)
        cls.bacalaos+=1
        return pez
    