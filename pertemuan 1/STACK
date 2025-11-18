class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        print(f"Push: {item}")

    def pop(self):
        if self.isEmpty():
            return "Stack kosong!"
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack kosong!"
        return self.items[-1]

    def display(self):
        print("Isi Stack:", self.items)


# Program utama
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()

print("Pop:", stack.pop())
stack.display()
print("Peek:", stack.peek())
