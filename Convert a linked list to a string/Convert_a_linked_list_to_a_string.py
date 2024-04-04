# Стрінга
def stringify(node):
    if isinstance(node, Node):
        curr_node = node
        result = str(curr_node.data) + ' -> '
        while curr_node.next:
            curr_node = curr_node.next
            result += str(curr_node.data) + ' -> '
        result += 'None'
        return result
    return 'None'
