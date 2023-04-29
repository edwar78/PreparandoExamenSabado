class Piloto:
    def __init__(self):
        self.__nombre=None
        self.__fechanacimiento=None
        self.__salarioanula=None
        self.__pais=None
        
    @property
    
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre (self,dato):
        self.__nombre=dato
    @property
    
    def fechanacimiento(self):
        return self.__fechanacimiento
    
    @fechanacimiento.setter
    def fechanacimiento (self,dato):
        self.__fechanacimiento=dato
    @property
    
    def salarioanula(self):
        return self.__salarioanula
    
    @salarioanula.setter
    def salarioanula (self,dato):
        self.__salarioanula=dato

    @property
    
    def pais(self):
        return self.__pais
    
    @pais.setter
    def pais (self,dato):
        self.__pais=dato