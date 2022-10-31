import numpy as np


class Grafo:
    __matriz = None     # matriz de aristas del grafo
    __etiquetas = None  # arreglo con las etiquetas de los nodos

    def __init__(self):
        cant = int(input('Cantidad de nodos: '))
        self.__matriz = np.zeros((cant, cant))
        self.__etiquetas = np.empty(cant, dtype=str)

    def agregarNodos(self):
        for i in range(len(self.__etiquetas)):
            self.__etiquetas[i] = input('Etiqueta del nodo {}: '.format(i))

    def nuevaArista(self, nodo1, nodo2):
        self.__matriz[nodo1][nodo2] = 1     # si es ponderado de coloca la ponderación en lugar de un 1
        
    def mostrarMatriz(self):
        print(self.__matriz)

    def adyacentes(self, nodo):
        adyac = []
        for i in range(len(self.__etiquetas)):
            if ((self.__matriz[nodo][i] ==1) or (self.__matriz[i][nodo] == 1)) and (nodo != i):     # mira las filas y columnas correspondientes al nodo
                adyac.append(i)                                                                     # omite los elementos de la diagonal principal
        return adyac
    
    def camino(self, nodo1, nodo2):
        pass
    
    def caminoMinimo(self, nodo1, nodo2):
        pass
    
    def conexo(self):
        pass
    
    def aciclico(self):
        pass
    
    def arbolAdyacencia(self):  # si es un grafo ponderado
        pass
    
    def REA(self):
        pass
    
    def REP(self):
        pass