class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def remove_duplicates(head):
    if head:
        curr = head
        while curr.next:
            if curr.data == curr.next.data:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
    else:
        return head
