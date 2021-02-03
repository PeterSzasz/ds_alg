# simple double-ended queue

class queue:
    '''simple queue with enqueue, dequeue, peek'''

    def __init__(self) -> None:
        self.data = []
        self.first = 0  # at the front, deq side
        self.last = 0   # at the back, enq side

    def enqueue(self, element) -> None:
        self.data.append(element)
        self.last += 1

    def dequeue(self):
        front_element = self.data.pop(self.first)
        return front_element

    def peek(self):
        return self.data[self.first]

    def size(self):
        return len(self.data)

    def empty(self):
        return len(self.data) == 0

if __name__ == "__main__":
    q = queue()
    for i in range(0, 9):
        q.enqueue(i)
    print(q.data)
    for _ in range(q.size()):
        print(q.dequeue())

    print("queue empty" if q.empty() else "not empty")