class Nodo:
    __dato = None
    __sig = None

    def __init__(self, dato):
        self.__dato = dato
        self.__sig = None

    def getDato(self):
        return self.__dato

    def setSiguiente(self, sig):
        self.__sig = sig

    def getSiguiente(self):
        return self.__sig
