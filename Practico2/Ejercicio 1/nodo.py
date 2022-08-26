class Nodo:
    __dato = None
    __sig = None

    def __init__(self, dato):
        self.__dato = dato
        self.__sig = None

    def setSiguiente(self, siguiente):
        self.__sig = siguiente

    def getSiguiente(self):
        return self.__sig

    def getDato(self):
        return self.__dato