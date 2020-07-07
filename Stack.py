class Stack:
    def __init__(self):
        self.l = list()

    def size(self):
        return len(self.l)

    def isEmpty(self):
        if len(self.l) == 0:
            return False
        else:
            return True

    def push(self, e):
        self.l.append(e)

    def top(self):
        return self.l[-1]

    def pop(self):
        if self.isEmpty() == False:
            return None
        else:
            return self.l.pop()