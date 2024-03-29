from .animal import Animal

class Mamifero (Animal):
    _listado =[]
    caballos = 0
    leones = 0
    def __init__(self, nombre="", edad=0, habitat="", genero="", pelaje = False ,patas=0):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)

    @classmethod
    def setListado(cls,listado):
        cls._listado = listado
    @classmethod
    def getListado(cls):
        return cls._listado
    def setPelaje(self, pelaje):
        self._pelaje = pelaje
    def isPelaje(self):
        return self._pelaje
    def setPatas(self,patas):
        self._patas = patas
    def getPatas(self):
        return self._patas
    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)
    @classmethod
    def crearCaballo(cls,nombre, edad, genero):
        mamifero = Mamifero(nombre, edad, "pradera",genero,True, 4)
        cls.caballos+=1
        return mamifero
    @classmethod
    def crearLeon(cls ,nombre, edad, genero):
        mamifero = Mamifero(nombre, edad, "selva",genero,True, 4)
        cls.leones+=1
        return mamifero

