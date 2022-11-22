class Alumno:
    __nombre:str
    __nota:int

    def __init__(self,nombre,nota):
        self.__nombre= nombre
        self.__nota= nota

    def isAprobado(self):
        if self.nota<5:
            return False
        else:
            return True
    @property
    def nombre(self):
        return self.__nombre
    @property
    def nota(self):
        return self.__nota

    def __str__(self):
        return f"Nombre: {self.nombre}\nNota: {self.nota}"
