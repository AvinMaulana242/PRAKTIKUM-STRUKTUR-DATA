class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueue: {item}")

    def dequeue(self):
        if self.isEmpty():
            return "Queue kosong!"
        return self.items.pop(0)

    def front(self):
        if self.isEmpty():
            return "Queue kosong!"
        return self.items[0]

    def display(self):
        print("Isi Queue:", self.items)


# Program utama
queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
queue.display()

print("Dequeue:", queue.dequeue())
queue.display()
print("Front:", queue.front())
