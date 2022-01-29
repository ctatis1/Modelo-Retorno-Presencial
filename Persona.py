class Persona():
    contador_persona = 0

    @classmethod
    def contadorPersonas(cls):
        cls.contador_persona +=1
        return cls.contador_persona
    def __init__(self, dosis,posibilidad):
        self.idPersona = Persona.contadorPersonas()
        self._dosis = dosis
        self._posibilidad = posibilidad

    def __str__(self):
        return f'Persona[ID: {self.idPersona}, Dosis: {self._dosis}, Posibilidad: {self._posibilidad}]'