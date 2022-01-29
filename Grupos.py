

class Grupos:
    def __init__(self, tipo,contagio):
        self._tipo = tipo
        self._contagio = contagio

    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def contagio(self):
        return self._contagio
    @contagio.setter
    def contagio(self, contagio):
        self._contagio =contagio

    def __str__(self):
        return f'Grupo Tipo: {self._tipo} \n Probabilidad de Contagio: {self._contagio}'


