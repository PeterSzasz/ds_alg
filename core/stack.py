class list_element:
    '''A singly linked list like object.'''
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class stack:
    '''Simple stack, with push, pop, peek.'''

    def __init__(self):
        self.head = list_element("head")
        self.size = 0

    def push(self, data):
        element = list_element(data)
        element.next = self.head.next
        self.head.next = element
        self.size += 1

    def pop(self):
        if self.empty():
            raise Exception("Stack is empty.")
        last_element = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return last_element.data

    def peek(self):
        if self.empty():
            raise Exception("Stack is empty.")
        return self.head.next.data

    def size(self):
        return self.size

    def empty(self):
        return self.size == 0

    def __str__(self):
        result = ""
        element = self.head
        while element != None:
            result += str(element.data) + " "
            element = element.next
        return result


if __name__ == "__main__":
    s = stack()
    print("load")
    for i in range(10):
        s.push(i)
        print(s.peek(), end=" ")
    print()

    print(f"print: {s}")

    print("\nunload")
    for i in range(10):
        print(s.pop(), end=" ")

    print("stack empty" if s.empty() else "not empty")