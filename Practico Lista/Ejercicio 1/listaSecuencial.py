import numpy as np
# []


class ListaSecuencial:
    __ultimo = None
    __cant = None
    __listaSec = None

    def __init__(self, cantidad):
        __ultimo = 0
        __cant = cantidad
    
    def crear(self):
        self.__listaSec = np.empty(self.__cant, dtype=int)

    def recuperar(self, posicion):
        return self.__listaSec[posicion]

    def insertar(self, posicion, dato):
        if (posicion == self.__ultimo + 1) and (posicion < self.__cant -1):
            self.__listaSec[posicion] = dato
            self.__ultimo += 1
        elif (posicion > 0) and (posicion <= self.__ultimo):
            if self.acceder(posicion) is None:
                self.__listaSec[posicion] = dato
            else:
                pass    #   desplazar posiciones e insertar

    def suprimir(self, posicion):
        if posicion == self.__ultimo:
            self.__ultimo -= 1
            del self.__listaSec[posicion]
        else:
            del self.__listaSec[posicion]    #   suprimir y luego desplazar posiciones

    def buscar(self, dato):
        i = 0
        band = False
        while (i <= ultimo) and (not band):
            if dato == self.recuperar(i):
                band = True
            else:
                i += 1
        return i