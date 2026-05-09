class Persona:
    _contador_turnos = 1

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.turno = Persona._contador_turnos
        Persona._contador_turnos += 1
