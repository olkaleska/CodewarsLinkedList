class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    counter = 1
#     curr = head
    if head:
        first_head = head
        first_curr = first_head
    else:
        raise TypeError
    if head.next:
        second_head = head.next
        second_curr = second_head
    else:
        raise TypeError
    curr = head.next
    while curr.next:
        if counter % 2 == 0:
            second_curr.next = curr.next
            counter += 1
            curr = curr.next
            second_curr = second_curr.next
        else:
            first_curr.next = curr.next
            counter += 1
            curr = curr.next
            first_curr = first_curr.next
    if counter % 2:
        first_curr.next = curr.next
    else:
        second_curr.next = curr.next

    return Context(first_head, second_head)
#     залтш обробити останнє
