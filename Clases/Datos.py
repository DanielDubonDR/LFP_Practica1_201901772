class Datos:
    def __init__(self, linea, identificador, lista, operacionO, operacionB, nBuscar):
        self.linea=linea
        self.identificador=identificador
        self.lista=lista
        self.operacionO=operacionO
        self.operacionB=operacionB
        self.nBuscar=nBuscar
    
    def getIdentifiador(self):
        return self.identificador
    
    def getLista(self):
        return self.lista

    def getOperacionO(self):
        return self.operacionO

    def getOperacionB(self):
        return self.operacionB
    
    def getNbuscar(self):
        return self.nBuscar