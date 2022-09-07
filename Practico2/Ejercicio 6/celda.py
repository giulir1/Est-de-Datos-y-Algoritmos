class Celda:
    __dato = 0
    __siguiente = None

    def __init__(self, dato=0):
        self.__dato = dato
        self.__siguiente = None

    def getDato(self):
        return self.__dato

    def setSiguiente(self, sig):
        self.__siguiente = sig

    def getSiguiente(self):
        return self.__siguiente
