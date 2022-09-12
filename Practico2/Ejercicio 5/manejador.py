from pilaSecuencial import Pila

import numpy as np

class Manejador:
    __pilas = None
    __cant = None
    __cont = 0
    def __init__(self, cant):
        self.__pilas = np.empty(3, dtype=Pila)
        self.__cant = cant
        self.__cont = 0
    def __str__(self):
        text  = ''
        for i in range(len(self.__pilas)):
            text += self.graficar(self.__pilas[i], i)
            text += '\n////////////////////////////////////////////////////'
        return text
    def escanear(self):
        cont = self.__pilas[2].mostrar()
        self.__pilas[2] = self.reLoad(cont)
        return cont
    def graficar(self, pila, pos):
        text = '\n|'
        disco = '-----'
        torre = pila
        contenido = torre.mostrar()
        #print(contenido)
        cont = 0
        if(len(contenido) > 0):
                for elemen in contenido:
                    text += '\n|'
                    text += '\n' + (disco * elemen)
        else:
                for i in range(self.__cant):
                    text += '\n|\n|'
        text += '\n|'
        self.__pilas[pos] = self.reLoad(contenido)
        return text
    def reLoad(self, contenido):
        contenido.sort(reverse = True) #invertimos la lista
        pila = Pila(self.__cant)
        for cont in contenido:
            pila.insertar(cont)
        return pila
    def cargarPila(self, pila):
        if(self.__cont < self.__cant):
            self.__pilas[self.__cont] = pila
            self.__cont += 1
    def moverTope(self, inicio, final):
        tope = self.__pilas[inicio-1].suprimir()
        self.__pilas[final-1].insertar(tope)
    def getTope(self, pos):
        return self.__pilas[pos-1].getTope()
    def getContTope(self, pos):
        return self.__pilas[pos-1].getContTope()
    def getLen(self):
        return len(self.__pilas)