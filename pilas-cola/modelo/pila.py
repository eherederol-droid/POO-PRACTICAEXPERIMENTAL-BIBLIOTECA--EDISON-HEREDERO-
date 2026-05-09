class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def top(self):
        if not self.isEmpty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def pushAll(self, other_pila):
        self.items.extend(other_pila.items)

    def reverse(self):
        new_pila = Pila()
        new_pila.items = self.items[::-1]
        return new_pila

    def copiar(self):
        nueva_pila = Pila()
        for item in self.items:
            nueva_pila.push(item)
        return nueva_pila

    def contiene(self, elemento) -> bool:
        for i in range(len(self.items)):
            if self.items[i] == elemento:
                return True
        return False

    def __str__(self):
        return str(self.items)
