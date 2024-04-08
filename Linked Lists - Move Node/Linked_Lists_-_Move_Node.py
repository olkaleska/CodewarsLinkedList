class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
        
    
def move_node(source, dest):
    if source:
        dest = Node(source.data, dest)
        if source.next:
            source = source.next
        else:
            source = None
        return Context(source, dest)
    else:
        raise ValueError
