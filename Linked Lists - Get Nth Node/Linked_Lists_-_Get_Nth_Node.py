from preloaded import Node

class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def get_nth(node, index):
    if index >= 0 and isinstance(index, int):
        curr = node
        counter = 0
        while curr:
            if counter == index:
                return curr
            curr = curr.next
            counter += 1
        raise TypeError
    raise TypeError
