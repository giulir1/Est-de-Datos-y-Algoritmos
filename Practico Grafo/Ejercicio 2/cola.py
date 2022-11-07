import numpy as np


class Cola:
    __cola = None
    __cant = 0
    __max = 0
    __ultimo = 0
    __primer = 0

    def __init__(self, xmax=0):
        self.__max = xmax
        self.__ultimo = 0
        self.__primer = 0
        self.__cant = 0
        self.__cola = np.empty(self.__max, dtype=str)

    def vacia(self):
        return self.__cant == 0

    def insertar(self, dato):
        insercion = dato
        if self.__cant < self.__max:        # si no está llena
            self.__cola[self.__ultimo] = dato
            self.__ultimo = (self.__ultimo + 1) % self.__max
            self.__cant += 1
            print('insertó')
        else:
            insercion = False
        return insercion

    def suprimir(self):
        if self.vacia():
            print('PILA VACIA - No se pudo suprimir.')
            x = False
        else:
            x = self.__cola[self.__primer]
            self.__primer = (self.__primer + 1) % self.__max
            self.__cant -= 1
        return x

    def recorrer(self):
        text = ''
        cant = self.__cant
        if not self.vacia():
            for i in range(cant):
                dato = self.suprimir()
                if dato is not False:
                    text += str(dato)
        return text
