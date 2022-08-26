from nodo import Nodo


class PilaEnlazada:
    __tope = -1
    __cant = 0

    def __init__(self, cant = 0):
        self.__tope = None
        self.__cant = cant

    def vacia(self):
        return self.__cant == 0
    
    def insertar(self, dato):
        unNodo = Nodo(dato)
        unNodo.setSiguiente(self.__tope)
        self.__tope = unNodo
        self.__cant += 1

    def suprimir(self):
        if self.vacia():
            print('ERROR - Pila vacia')
        else:
            aux = self.__tope.getSiguiente()
            datoTope = self.__tope.getDato()
            del(self.__tope)
            self.__cant -= 1
            self.__tope = aux
            return datoTope
