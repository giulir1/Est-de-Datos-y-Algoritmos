import numpy as np
from nodo import Nodo
# factor de carga de 0,7


class Hash:
    __arreglo = None

    def __init__(self):
        tamano = 23
        self.__arreglo = np.empty(tamano, dtype=Nodo)
        for i in range(len(self.__arreglo)):
            self.__arreglo[i] = Nodo(None)

    def funcionHash(self, clave):
        partes = []
        clave = str(clave)
        longi = len(clave)
        longiTabla = len(self.__arreglo)
        print('longitud = {}'.format(longiTabla))
        for i in range(len(clave)):
            print(longi)
            if longi >= 0:
                partes.append(clave[longi-longiTabla:longi])
                longi -= longiTabla
                print(longi)
        print(partes)

    def hash(self, clave):
        modulo = int(clave) % 23
        return modulo

    def agregar(self, clave):
        pos = self.hash(clave)
        if self.__arreglo[pos].getDato() is None:
            self.__arreglo[pos] = Nodo(clave)
        else:
            anterior = self.__arreglo[pos]
            aux = self.__arreglo[pos].getSiguiente()
            while aux is not None:
                anterior = aux
                aux = self.__arreglo[pos].getSiguiente()
            aux = Nodo(clave)
            anterior.setSiguiente(aux)

    def mostrar(self):
        for i in range(len(self.__arreglo)):
            print(self.__arreglo[i].getDato())
            if self.__arreglo[i].getSiguiente() is not None:
                print('entró a la lista de sinonimos')
                aux = self.__arreglo[i].getSiguiente()
                while aux is not None:
                    print(aux.getDato())
                    aux = aux.getSiguiente()

    def buscar(self, clave):
        band = False
        pos = self.hash(clave)
        if self.__arreglo[pos].getDato() == clave:
            print('Se encontró la clave {} en la componente N° {} del arreglo.'.format(clave, pos))
            band = True
        else:
            if self.__arreglo[pos].getSiguiente() is not None:
                print('entro if buscar')
                aux = self.__arreglo[pos].getSiguiente()
                while aux is not None:
                    print('entro al while')
                    if aux.getDato() == clave:
                        print('Se encontró la clave {} en la componente N° {} del arreglo.'.format(clave, pos))
                        band = True
                        aux = aux.getSiguiente()
        if not band:
            print('No se encontró la clave {}.'.format(clave))

    def colision(self):
        pass
