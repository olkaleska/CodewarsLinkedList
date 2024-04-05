class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next #changed a Node a bit

def push(head, data):
    if head is not None:
        old_node = Node(head.data, head.next)
        new_head = Node(data, old_node)
    else:
        new_head = Node(data, None)
    return new_head

def build_one_two_three():
    first = push(None, 3)
    second = push(first, 2)
    return push(second, 1)
