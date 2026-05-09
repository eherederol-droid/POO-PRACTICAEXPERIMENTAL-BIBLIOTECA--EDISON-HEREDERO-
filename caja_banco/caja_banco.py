from modelo.persona import Persona
from modelo.cola import Cola

class CajaBanco:
    def __init__(self):
        self.fila = Cola()

    def agregar_persona(self, persona: Persona):
        self.fila.push(persona)

    def esta_vacia(self) -> bool:
        return self.fila.isEmpty()

    def atender(self) -> Persona:
        if not self.esta_vacia():
            return self.fila.pop()
        return None

    def persona_abandona(self, nombre: str) -> bool:
        cola_temp = Cola()
        encontrado = False

        # Extraer elementos de la cola original
        while not self.fila.isEmpty():
            p = self.fila.pop()
            if not encontrado and p.nombre == nombre:
                encontrado = True
                # No lo agregamos a la temporal, así lo eliminamos
            else:
                cola_temp.push(p)

        # Volver a pasar los elementos a la cola original
        while not cola_temp.isEmpty():
            self.fila.push(cola_temp.pop())

        return encontrado
