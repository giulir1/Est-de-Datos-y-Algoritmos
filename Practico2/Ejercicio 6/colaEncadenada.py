from celda import Celda


class ColaEncadenada:
    __cant = 0
    __primer = None
    __ultimo = None

    def __init__(self, cant=0):
        self.__cant = cant

    def vacia(self):
        return self.__cant == 0

    def insertar(self, dato):
        aux = Celda(dato)
        aux.setSiguiente(None)
        if self.__ultimo is None:
            self.__primer = aux
            self.__ultimo = aux
            self.__cant += 1
        else:
            self.__ultimo.setSiguiente(aux)
            self.__ultimo = aux
            self.__cant += 1
        return self.__ultimo.getDato()

    def suprimir(self):
        if self.vacia():
            print('Cola vacía.')
            x = -1
        else:
            aux = self.__primer
            x = aux.getDato()
            self.__primer = self.__primer.getSiguiente()
            self.__cant -= 1
            print(type(self.__primer))
            if self.__primer is None:
                self.__ultimo = None
            del aux
        return x

    def recorrer(self):
        aux = self.__primer
        while aux is not None:
            dato = aux.getDato()
            print(dato)
            aux = aux.getSiguiente()
