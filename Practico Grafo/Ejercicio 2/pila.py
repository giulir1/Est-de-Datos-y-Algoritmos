import numpy as np
# [ ]


class Pila:
    __tope = None
    __cant = None
    __pila = None

    def __init__(self, cant=0):
        self.__tope = -1
        self.__cant = cant
        self.__pila = None

    def vacia(self):
        return self.__tope == -1

    def crear(self):                                    # para poder insertar, suprimir o recorrer primero se debe crear la pila
        self.__pila = np.empty(self.__cant, dtype=int)

    def insertar(self, x):
        if self.__tope < (self.__cant - 1):
            self.__tope += 1
            self.__pila[self.__tope] = x
            num = x
        else:
            num = 0
        return num

    def suprimir(self):
        if not self.vacia():
            num = self.__pila[self.__tope]
            np.delete(self.__pila, self.__tope)
            self.__tope -= 1
        else:
            print('ERROR - Pila vacia')
            num = False
        return num

    def mostrar(self):
        i = 0
        text = ''
        if not self.vacia():
            tope = self.__tope
            while i <= tope:
                num = self.suprimir()
                text += str(num)
                i += 1
        else:
            print('ERROR - Pila vacia')
        return text
