import numpy as np
from nodo import Nodo
# factor de carga de 0,7


class Hash:
    __arreglo = None

    def __init__(self):
        tamano = 211
        self.__arreglo = np.empty(tamano, dtype=Nodo)

    def funcionHash(self, clave):
        partes = []
        clave = str(clave)
        longi = len(clave)
        longiTabla = len(self.__arreglo)
        print('longitud = {}'.format(longiTabla))
        if longi >= longiTabla:
            for i in range(len(clave)):
                print(longi)
                if longi >= 0:
                    partes.append(clave[longi-longiTabla:longi])
                    longi -= longiTabla
                    print(longi)
            print(partes)


    def agregar(self, clave):
        pass

    def colision(self):
        pass