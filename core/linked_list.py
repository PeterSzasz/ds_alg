# singly and doubly linked list
# with add to head and tail, remove nth

class LinkedList_singly():
    class Node():
        def __init__(self, data, next = None):
            self.data = data
            self.next = next

        def __str__(self):
            next_node = "None"
            if self.next:
                next_node = self.next.data
            return f"[{self.data} -> {next_node}]"

    def __init__(self) -> None:
        self.head = self.Node("head")
        self.tail = self.Node("tail")
        self.head.next = self.tail

    def next_node(self):
        n = self.head
        while n != None:
            yield n
            n = n.next

    def add_head_node(self, data):
        new_node = self.Node(data, self.head.next)
        self.head.next = new_node

    def add_tail_node(self, data):
        last_node = None
        for node in self.next_node():
            if node.next.data == "tail":
                last_node = node
                break
        new_node = self.Node(data, self.tail)
        last_node.next = new_node

    def add_nth_node(self, data, n):
        if n == 0:
            raise("Cannot replace head node!")
        if n == 2 + self.size():
            raise("Cannot replace tail node!")
        if n > 2 + self.size():
            raise("Invalid node number!")
        i = 0
        prev_node = self.head
        for node in self.next_node():
            if i == n:
                new_node = self.Node(data)
                prev_node.next = new_node
                new_node.next = node
            i += 1
            prev_node = node

    def size(self):
        result = 0
        for _ in self.next_node():
            result += 1
        return result - 2   # minus head and tail

    def remove_node(self, n):
        if n == 0:
            raise("Cannot delete head node!")
        if n == 1 + self.size():
            raise("Cannot delete tail node!")
        if n > 1 + self.size():
            raise("Invalid node number!")
        i = 0
        prev_node = self.head
        for node in self.next_node():
            if i == n:
                prev_node.next = node.next
                node.next = None
                node.data = None
                node = None
            i += 1
            prev_node = node




class LinkedList_doubly(LinkedList_singly):
    class DNode():
        def __init__(self, data, prev = None, next = None):
            self.data = data
            self.next=next
            self.prev = prev

        def __str__(self):
            next_node = "None"
            prev_node = "None"
            if self.next:
                next_node = self.next.data
            if self.prev:
                prev_node = self.prev.data
            return f"[{prev_node} <- {self.data} -> {next_node}]"

    def __init__(self) -> None:
        self.head = self.DNode("head", None, None)
        self.tail = self.DNode("tail", self.head, None)
        self.head.next = self.tail

    def prev_node(self):
        n = self.tail
        while n != None:
            yield n
            n = n.prev

    def add_head_node(self, data):
        first_node = self.head.next
        new_node = self.DNode(data, self.head, self.head.next)
        self.head.next = new_node
        first_node.prev = new_node

    def add_tail_node(self, data):
        last_node = self.tail.prev
        new_node = self.DNode(data, last_node, self.tail)
        self.tail.prev = new_node
        last_node.next = new_node

    def add_nth_node(self, data, n):
        '''adds a node to the n-th place and shifts up remaining nodes'''
        if n == 0:
            raise("Cannot replace head node!")
        if n == 2 + self.size():
            raise("Cannot replace tail node!")
        if n > 2 + self.size():
            raise("Invalid node number!")
        i = 0
        for node in self.next_node():
            if n == i:
                new_node = self.DNode(data, node.prev, node)
                node.prev.next = new_node
                node.prev = new_node
            i += 1

    def remove_node(self, n):
        if n == 0:
            raise("Cannot delete head node!")
        if n == 1 + self.size():
            raise("Cannot delete tail node!")
        if n > 1 + self.size():
            raise("Invalid node number!")
        i = 0
        for node in self.next_node():
            if n == i:
                node.prev.next = node.next
                node.next.prev = node.prev
                node.data = None
                node.prev = None
                node.next = None
                node = None
            i += 1
