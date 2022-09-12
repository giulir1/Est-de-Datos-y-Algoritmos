from cajero import Cajero

from colaSecuencial import ColaS

from colaEncadenada import ColaE

from manejador import Manejador

def consultorio(manejador): #crea la cola del consultorio
    consultorio = ColaE()
    manejador.addConsultorio(consultorio)
def especialidad(manejador): #crea la cola de las especialidades
    especialidades = ['Ginecologia', 'Clinica medica', 'Oftamologia', 'Pediatria']
    for especialidad in especialidades:
        cola = ColaS(10, especialidad)
        manejador.addCola(cola)
if __name__ == '__main__':
    manejador = Manejador()
    cajero = Cajero(2)
    manejador.addCajero(cajero)
    consultorio(manejador) #Intentar con la cola escalonada
    especialidad(manejador)
    tiempo1 = 0
    tiempo2 = 0
    band = True
    print('-----LA SIMULACIÓN ARRANCARÁ EN LA HORA 05:00-----')
    while tiempo1 < 240: #4 horas = 240 minutos
        #print(tiempo1)
        manejador.addPacienteCola(0) 
        if(tiempo1 > 120): # hace que se forme una cola a partir de las 5hrs
            manejador.atencion(band)
        if(tiempo2 == 180): #tiempo de atención del consultorio de 7hrs a 8hrs
            band = False
            tiempo2 += 1
        elif(tiempo2 < 120): #Tiempo máximo de ateción
            tiempo2 += 1
        else: #los médicos empiezan atender
            manejador.atencionMed()
        tiempo1 += 1
    #print(manejador.mostrarE())
    #mostrar los promedios y cantidad de pacientes no atendidos
    print('-----FIN DE LA SIMULACIÓN-----\n\nCantidad de pacientes sin turnos: {}\n'.format(manejador.cantSinTurnos()))
    print('PROMEDIOS DE ESPERA:')
    print('{}'.format(manejador.promEspera()))
    print('{}'.format(manejador.promColas()))
    input()