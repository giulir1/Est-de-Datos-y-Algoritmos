import numpy as np

from cliente import Cliente

class Cola:
    __arreglo = None
    __max = None
    __primer = 0
    __ultimo = 0
    __cant = 0
    def __init__(self, max = 0):
        self.__arreglo = np.empty(max, dtype=Cliente)
        self.__max = max
        self.__primer = 0
        self.__ultimo = 0
        self.__cant = 0
    def vacia(self):
        return self.__cant == 0
    def insertar(self, dato):
        if(self.__cant < self.__max):
            self.__arreglo[self.__ultimo] = dato
            self.__ultimo = (self.__ultimo + 1) % self.__max
            self.__cant+=1
            #print(self.__ultimo)
            return dato
        else:
            return 0
    def suprimir(self):
        if(self.vacia()):
            print('Pila vacía')
            return -1
        else:
            x = self.__arreglo[self.__primer]
            self.__primer = (self.__primer+1) % self.__max
            self.__cant -= 1
            #print(self.__primer)
            return x
    def getCant(self):
        return self.__cant


    def recorrer(self): #revisar
        contenido = []
        #print('Primer: ',self.__primer)
        if(not self.vacia()):
            for i in range(self.__cant):
                cliente = self.suprimir()
                if(cliente != -1):
                    contenido.append(cliente)
        return contenido