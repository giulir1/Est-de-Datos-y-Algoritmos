class Celda:
    __dato = None
    __siguiente = None
    def __init__(self, dato = None):
        self.__dato = dato
        self.__siguiente = None
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente
    def getSiguiente(self):
        return self.__siguiente
    def loadDato(self, dato): #no es necesario
        self.__dato = dato
    def getDato(self):
        return self.__dato
    def __str__(self):
        return ''.format(self.__dato)