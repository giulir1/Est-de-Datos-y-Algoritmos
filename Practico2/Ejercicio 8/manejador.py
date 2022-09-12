class Manejador:
    __colas = None
    __consultorio = None
    __cajero = None
    __medicos = None
    __medAtencion = None
    __i = None
    def __init__(self):
        self.__colas = []
        self.__consultorio = None
        self.__cajero = None
        self.__medicos = []
        self.__medAtencion = []
        self.__i = 0
    def addCola(self, cola):
        self.__colas.append(cola)
        self.__medicos.append(0) #se agrega un médico a la especialidad
        self.__medAtencion.append(0)
    def addConsultorio(self, consultorio):
        self.__consultorio = consultorio
    def addPacienteCola(self, paciente): #añade un paciente a la cola del consultorio
        self.__consultorio.insertar(paciente)
        #print('Nuevo Paciente')
    def addCajero(self, cajero):
        self.__cajero = cajero
    def colasLlenas(self):
        band = False
        cont = 0
        for cola in self.__colas:
            if(cola.llena()):
                cont += 1
        if(cont == len(self.__colas)):
            band = True
        return band
    def aumentarTiempoConsul(self):
        pacientes = self.__consultorio.recorrer()
        for paciente in pacientes:
            paciente += 1
            self.__consultorio.insertar(paciente)
    def aumentarTiempoColas(self):
        for cola in self.__colas:
            pacientes = cola.recorrer()
            for paciente in pacientes:
                paciente += 1
                cola.insertar(paciente)
    def pasarPaciente(self, paciente):
        if(self.__i < len(self.__colas)):
            self.__colas[self.__i].insertar(paciente)
            self.__i += 1
        else:
            self.__i = 0
            self.__colas[self.__i].insertar(paciente)
            self.__i += 1
    def atencion(self, band):
        if(self.__cajero.getEstado() == None and not self.__consultorio.vacia() and band): #añade paciente al cajero
            #print('atiende')
            paciente = self.__consultorio.suprimir()
            self.__cajero.setCliente(paciente)
        paciente = self.__cajero.aumentarTiempo() #aumenta el tiempo del cajero
        #pasar paciente a las colas
        if(paciente != None and not self.colasLlenas()):
            self.pasarPaciente(paciente)
        elif(self.colasLlenas()):
            self.addPacienteCola(paciente)
        self.aumentarTiempoConsul()
        self.aumentarTiempoColas()
    def atencionP(self, pos): #cuenta el tiempo de atención por paciente
        if(self.__medicos[pos] < self.__medAtencion[pos]):
            self.__medicos[pos] += 1
            #print('Medico {}: {}'.format(pos, self.__medicos[pos]))
        else:
            self.__medicos[pos] = 0
    def atencionMed(self):
        for i in range(len(self.__colas)):
            if(not self.__colas[i].vacia() and self.__medicos[i] == 0):
                #print('Medico {} -ATIENDE PACIENTE-'.format(i))
                self.__medicos[i] = self.__colas[i].suprimir()
                self.__medAtencion[i] = self.__medicos[i] + 20 #tiempo máximo
            elif(self.__medicos[i] > 0):
                self.atencionP(i)
    def calcProm(self, cola):
        prom = 0
        cant = cola.getCant()
        for i in range(cant):
            prom += cola.suprimir()
        try:
            prom /= cant
        except ZeroDivisionError:
            print('ERROR: no hay promedio')
        return prom
    def promColas(self):
        promedio = ''
        for cola in self.__colas:
            promedio += '{}: '.format(cola.getNombre())
            promedio += '{}\n'.format(self.calcProm(cola))
        return promedio
    def promEspera(self):
        promedio = 'Consultorio: '
        promedio += '{}'.format(self.calcProm(self.__consultorio))
        return promedio
    def cantSinTurnos(self):
        return self.__consultorio.getCant()
    def mostrarE(self):
        print('Consultorio: ', self.__consultorio.recorrer())
        #self.__consultorio.mostrar()
        for cola in self.__colas:
            print('Cola', cola.recorrer())