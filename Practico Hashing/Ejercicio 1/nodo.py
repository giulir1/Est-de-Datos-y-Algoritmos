class Nodo:
    __dato = None
    __sig = None

    def __init__(self, dato):
        self.__dato = dato

    def getDato(self):
        return self.__dato

    def setSiguiente(self, sig):
        self.__sig = sig

    def getSiguiente(self, sig):
        return self.__sig