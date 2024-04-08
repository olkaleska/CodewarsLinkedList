# 
class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next


def linked_list_from_string(s):
    splited = s.split(' -> ')[::-1]
    splited[0] = None
    for i, el in enumerate(splited):
        head = None
        if el == None:
            pass
        elif i == 1:
            node = Node(int(el), None)
            curr = node
        elif i == len(splited) - 1:
            head = Node(int(el), curr)
        else:
            node = Node(int(el), curr)
            curr = node
    return head
