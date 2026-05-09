class Cola:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return None

    def top(self):
        if not self.isEmpty():
            return self.items[0]
        return None

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def pushAll(self, other_cola):
        self.items.extend(other_cola.items)

    def reverse(self):
        new_cola = Cola()
        new_cola.items = self.items[::-1]
        return new_cola

    def copiar(self):
        nueva_cola = Cola()
        for item in self.items:
            nueva_cola.push(item)
        return nueva_cola

    def contiene(self, elemento) -> bool:
        for i in range(len(self.items)):
            if self.items[i] == elemento:
                return True
        return False

    def __str__(self):
        return str(self.items)
