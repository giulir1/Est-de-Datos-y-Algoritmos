import numpy as np
# [ ]


class PilaSecuencial:
    __tope1 = None
    __tope2 = None
    __cant = None
    __pila = None

    def __init__(self, cant=0):
        self.__tope1 = -1
        self.__tope2 = cant
        self.__cant = cant
        self.__pila = None

    def vaciaPila1(self):
        return self.__tope1 == -1

    def vaciaPila2(self):
        return self.__tope2 == self.__cant + 1

    def pilaLlena(self):
        return self.__tope1 == self.__tope2 - 1

    def crear(self):                                    # para poder insertar, suprimir o recorrer primero se debe crear la pila
        self.__pila = np.empty(self.__cant, dtype=int)

    def insertarPila1(self, x):
        if self.__tope1 < (self.__cant - 1):
            if self.__tope1 == self.__tope2 - 1:
                num = False
            else:
                self.__tope1 += 1
                self.__pila[self.__tope1] = x
                num = x
        else:
            num = False
        return num

    def suprimirPila1(self):
        if not self.vaciaPila1():
            num = self.__pila[self.__tope1]
            np.delete(self.__pila, self.__tope1)
            self.__tope1 -= 1
        else:
            print('ERROR - Pila vacia')
            num = False
        return num

    def mostrarPila1(self):
        i = 0
        text = ''
        if not self.vaciaPila1():
            tope = self.__tope1
            while i <= tope:
                num = self.suprimirPila1()
                text += str(num)
                i += 1
        else:
            print('ERROR - Pila vacia')
        return text

    def insertarPila2(self, x):
        if self.__tope2 > self.__tope1:
            if self.__tope1 == self.__tope2 - 1:
                num = False
            else:
                self.__tope2 -= 1
                self.__pila[self.__tope2] = x
                num = x
        else:
            num = False
        return num

    def suprimirPila2(self):
        if not self.vaciaPila2():
            num = self.__pila[self.__tope2]
            np.delete(self.__pila, self.__tope2)
            self.__tope2 += 1
        else:
            print('ERROR - Pila vacia')
            num = False
        return num

    def mostrarPila2(self):
        i = 0
        text = ''
        if not self.vaciaPila2():
            tope = self.__tope2
            while i <= tope:
                num = self.suprimirPila2()
                text += str(num)
                i += 1
        else:
            print('ERROR - Pila vacia')
        return text
