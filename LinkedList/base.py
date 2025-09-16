''' 
Linked List from scratch
'''

class Node: 
    def __init__(self, value): 
        self.value = value
        self.next = None

# Linked list with initial element
class LinkedList: 
    def __init__(self, value): 
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

# Empty Linked List
class LinkedList: 
    def __init__(self): 
        self.head = None
        self.tail = None
        self.length = 0

# Instanciate the Linked List
linked_list = LinkedList(10)
print(linked_list)