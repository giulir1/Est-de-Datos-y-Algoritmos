from nodo import Nodo

# {}
class arbol:
    __raiz = None

    def __init__(self):
        self.__raiz = None
    
    def vacio(self):
        return self.__raiz == None

    def getRaiz(self):
        return self.__raiz

    def mostrarRaiz(self):
        return self.__raiz.getDato()

    def insertarRaiz(self, dato):
        raiz = Nodo(dato)
        self.__raiz = raiz

    def buscar(self, arbol, dato):
        if self.vacio():
            print('ERROR - El arbol esta vacio.')
        else:
            if self.__raiz.getDato() == dato:
                print('El dato "{}" se encuentra en el arbol.')
            else:
                if dato < self.__raiz.getDato():
