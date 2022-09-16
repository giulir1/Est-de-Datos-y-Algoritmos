class Nodo:
    __dato = None
    __izq = None
    __der = None

    def __init__(self, dato, izq=None, der=None):
        self.__dato = dato
        self.__izq = izq
        self.__der = der

    def setDato(self, dato):
        self.__dato = dato

    def getDato(self):
        return self.__dato

    def setIzq(self, izq):
        self.__izq = izq

    def getIzq(self):
        return self.__izq

    def setDer(self, der):
        self.__der = der

    def getDer(self):
        return self.__der

    