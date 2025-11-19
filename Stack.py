from Node import Node
class Stack:
    def __str__(self):
        values = []
        current = self.top
        while current:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values) + " -> None"
    
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return None
        val = self.top.value
        self.top = self.top.next
        return val

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(s)