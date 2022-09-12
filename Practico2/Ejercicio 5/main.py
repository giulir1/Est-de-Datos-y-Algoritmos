import os

from controlador import Controlador

from manejador import Manejador

from pilaSecuencial import Pila

def init(dificultad):
    lista = []
    for i in range(3):
        pila = Pila(dificultad)
        if(i == 0):
            for disc in range(dificultad, 0, -1):
                pila.insertar(disc)
        lista.append(pila)
    return lista
def load(manejador, pilas):
    for pila in pilas:
        manejador.cargarPila(pila)
if __name__ == '__main__':
    ctrl = Controlador()
    dif = int(input('Ingrese cantidad de discos: '))
    manejador = Manejador(dif)
    pilas = init(dif)
    load(manejador, pilas)
    ctrl.moveOp(dif)
    ctrl.loadManejador(manejador)
    band = False
    fin = False
    while not band:
        print(ctrl.mostrar())
        print('PARA FINALIZAR INGRESE "Fin"')
        print('-----CANTIDAD DE MOVIMIENTOS: {}-----'.format(ctrl.getMovimientos()))
        orden1 = input('Sacar disco: ')
        if(orden1.lower() != 'fin'):
            if(ctrl.loadOrdenI(orden1)):
                orden2 = input('Poner disco: ')
                if(ctrl.loadOrdenF(orden2)):
                    ctrl.mover()
            if(ctrl.escanear(dif)):
                band = True
                fin = True
        else:
            band = True
        os.system('cls')
    print('-----FIN DEL JUEGO-----\n')
    if(ctrl.puntaje() and fin):
        print('RESULTADO DE MOVIMIENTOS: {}\n -----FUE LA MEJOR-----'.format(ctrl.getMovimientos()))
    elif(fin):
        print('RESULTADO DE MOVIMIENTOS: {}\n -----SE PUEDE MEJORAR-----'.format(ctrl.getMovimientos()))
    input()