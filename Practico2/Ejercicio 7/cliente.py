class Cliente:
    __tiempo = 0
    def __init__(self, tiempo = 0):
        self.__tiempo = tiempo
    def incrementarTiempo(self):
        self.__tiempo += 1
    def getTiempo(self):
        return self.__tiempo