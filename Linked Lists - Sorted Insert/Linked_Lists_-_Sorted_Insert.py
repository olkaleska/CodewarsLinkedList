""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""
class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def sorted_insert(head, data):
    if head is None or data <= head.data:
        head = Node(data, head)
        return head
    curr = head
    while curr.next:
        if data > curr.next.data:
            curr = curr.next
        else:
            new = Node(data, curr.next)
            curr.next = new
            return head
    new = Node(data)
    curr.next = new
    return head
