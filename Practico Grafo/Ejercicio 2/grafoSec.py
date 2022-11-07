import numpy as np
from pila import Pila
from cola import Cola


class GrafoSec:
    __matriz = None     # matriz de aristas del grafo
    __etiquetas = None  # arreglo con las etiquetas de los nodos

    def __init__(self):
        cant = int(input('Cantidad de nodos: '))
        self.__matriz = np.zeros((cant, cant))
        self.__etiquetas = np.empty(cant, dtype=str)

    def agregarNodos(self):
        for i in range(len(self.__etiquetas)):
            self.__etiquetas[i] = input('Etiqueta del nodo {}: '.format(i))

    def getPosNodo(self, etiqueta):     # ingreso la etiqueta del nodo y devuelve la posicion para buscarlo
        i = 0
        band = False
        while (i < len(self.__etiquetas)) and (not band):
            if self.__etiquetas[i] == etiqueta:
                band = True
            else:
                i += 1
        if band:
            nodo = i
        else:
            nodo = None
        return nodo

    def nuevaArista(self, nodo1, nodo2):    # deberia ingresar las etiquetas y devolver la posicion con el metodo getPosNodo
        self.__matriz[nodo1][nodo2] = 1     # si es ponderado de coloca la ponderación en lugar de un 1

    def mostrarMatriz(self):
        print(self.__matriz)

    def adyacentes(self, etiqueta):
        adyac = []
        nodo = self.getPosNodo(etiqueta)
        for i in range(len(self.__etiquetas)):
            if ((self.__matriz[nodo][i] == 1) or (self.__matriz[i][nodo] == 1)) and (nodo != i):     # mira las filas y columnas correspondientes al nodo
                adyac.append(self.__etiquetas[i])                                                                     # omite los elementos de la diagonal principal
        return adyac

    def caminoNodo(self, etiqueta):     # nodos a los que sale el nodo origen
        adyac = []
        nodo = self.getPosNodo(etiqueta)
        for i in range(len(self.__etiquetas)):
            if (self.__matriz[nodo][i] == 1) and (nodo != i):     # mira las filas y columnas correspondientes al nodo
                adyac.append(self.__etiquetas[i])                                                                     # omite los elementos de la diagonal principal
        return adyac

    def camino(self, nodo1, nodo2):
        caminoNodos = self.REA(nodo1)
        band = False
        i = 0
        while (i < len(caminoNodos)) and (not band):
            if caminoNodos[i] == nodo2:
                band = True
            else:
                i += 1
        return band

    def caminoMinimo(self, nodo1, nodo2):
        pass

    def conexo(self):
        pass

    def aciclico(self):
        pass

    def arbolAdyacencia(self):  # si es un grafo ponderado
        pass

    def REA(self, u):
        recorrido = []
        posicion = self.getPosNodo(u)
        if posicion is not None:
            listaNodos = []
            for i in range(len(self.__etiquetas)):
                listaNodos.append(-1)
            listaNodos[posicion] = 0
            cola = Cola(len(self.__etiquetas))
            cola.insertar(u)
            while not cola.vacia():
                v = cola.suprimir()
                recorrido.append(v)
                adyacentes = self.caminoNodo(v)
                for nodo in adyacentes:
                    posicion = self.getPosNodo(nodo)
                    if (posicion is not None) and (listaNodos[posicion] == -1):
                        listaNodos[posicion] = 1
                        cola.insertar(nodo)
        else:
            recorrido = None
        return recorrido

    def REP(self, u):
        recorrido = []
        posicion = self.getPosNodo(u)
        if posicion is not None:
            listaNodos = []
            for i in range(len(self.__etiquetas)):
                listaNodos.append(-1)
            listaNodos[posicion] = 0
            pila = Pila(len(self.__etiquetas))
            pila.insertar(u)
            while not pila.vacia():
                v = pila.suprimir()
                recorrido.append(v)
                adyacentes = self.caminoNodo(v)
                for nodo in adyacentes:
                    pos = self.getPosNodo(nodo)
                    if (posicion is not None) and (listaNodos[posicion] == -1):
                        listaNodos[posicion] = 1
                        pila.insertar(nodo)
        else:
            recorrido = None
        return recorrido

    def gradoSalida(self, etiqueta):
        adyac = self.caminoNodo(etiqueta)
        return len(adyac)

    def gradoEntrada(self, etiqueta):
        grado = 0
        nodo = self.getPosNodo(etiqueta)
        for i in range(len(self.__etiquetas)):
            if self.__matriz[i][nodo] == 1:
                grado += 1
        return grado

    def fuente(self, etiqueta):
        band = False
        if (self.gradoEntrada(etiqueta) == 0) and (self.gradoSalida(etiqueta) > 0):
            band = True
        return band

    def sumidero(self, etiqueta):
        band = False
        if (self.gradoEntrada(etiqueta) > 0) and (self.gradoSalida(etiqueta) == 0):
            band = True
        return band
