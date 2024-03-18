import zooAnimales

class Animal:
    _totalAnimales = 0
    def __init__(self,nombre="",edad=0,habitat="",genero=""):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        Animal._totalAnimales+= 1

    @classmethod
    def totalPorTipo(cls):
        cadena = "Mamiferos : " + str(len(zooAnimales.mamifero.Mamifero.getListado()))+"\nAves : " + str(len(zooAnimales.ave.Ave.getListado()))+"\nReptiles : " + str(len(zooAnimales.reptil.Reptil.getListado())) +"\nPeces : " + str(len(zooAnimales.pez.Pez.getListado()))+"\nAnfibios : " + str(len(zooAnimales.anfibio.Anfibio.getListado()))
        return cadena
    def toString(self):
        statement = ""
        if self._zona== None:
            statement = "Mi nombre es "+ str(self._nombre)+", tengo una edad de "+ str(self._edad)+", habito en "+ self._habitat+ " y mi genero es "+self._genero
        else :
            statement = "Mi nombre es "+ self._nombre+", tengo una edad de "+ self._edad+", habito en "+ self._habitat+ " y mi genero es "+self._genero+", la zona en la que me ubico es "+self._zona.getNombre()+" en el "+self._zona.getZoo().getNombre()
        return statement
    @staticmethod
    def movimiento():
        cadena = "desplazarse"
        return cadena
    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales
    def getNombre(self):
        return self._nombre
    def getEdad(self):
        return self._edad
    def getHabitat(self):
        return self._habitat
    def getGenero(self):
        return self._genero
    def getZona(self):
        return self._zona
    @classmethod
    def setTotalAnimales(cls, totalAnimales):
        cls._totalAnimales= totalAnimales
    def setNombre(self, nombre):
        self._nombre = nombre
    def setEdad(self,edad):
        self._edad= edad
    def setHabitat(self,habitat):
        self._habitat = habitat
    def setGenero(self, genero):
        self._genero = genero
    def setZona(self,zona):
        self._zona = zona
    
        