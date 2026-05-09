class Cola:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return None

    def isEmpty(self):
        return len(self.items) == 0
