# Queue

# Queue class
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            print('No item in Queue')
        self.items.pop(0)

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(1)
    print("After enqueuing 1:  " + str(queue))

    queue.enqueue(2)
    print("After enqueuing 2:  " + str(queue))

    queue.enqueue(50)
    print("After enqueuing 50:  " + str(queue))

    queue.dequeue()
    print("After dequeuing:  " + str(queue))

    queue.enqueue(5)
    print("After enqueuing 5:  " + str(queue))
