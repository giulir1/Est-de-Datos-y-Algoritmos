from cajero import Cajero

from cliente import Cliente

from manejador import Manejador

from colaSecuencial import Cola

if __name__ == '__main__':
    cola = Cola(20)
    tds = int(input('Tiempo de simulacion (minutos): '))
    atencion = int(input('Tiempo de atencion (minutos): '))
    llegada = int(input('Frecuencia de llegada de cliente (minutos): '))
    cajero = Cajero(atencion)
    manejador = Manejador(cajero, cola)
    tiempo1 = 0
    tiempo2 = 0
    while tiempo1 < tds:
        #print(tiempo1)
        if(tiempo2 == llegada): #tiempo de llegada de un cliente
            cliente = Cliente(-1) #crea un cliente
            manejador.llegadaCliente(cliente) #añade un cliente
            tiempo2 = 0
            #print('LLEGA')
        if(manejador.atencion()):
            manejador.aumentarTiempoCajero()
        manejador.aumentarTiempoCola()
        tiempo2 += 1
        tiempo1 += 1
    
    max = manejador.getMax()
    if(max != 0):
        print('-----TIEMPO MAXIMO ESPERADO: {}-----'.format(max))
    else:
        print('-----NO HAY UN TIEMPO MÁXIMO-----')