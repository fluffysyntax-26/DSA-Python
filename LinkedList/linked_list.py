class Node: 
    def __init__(self, value): 
        self.value = value
        self.next = None

class LinkedList: 
    def __init__(self): 
        self.head = None
        self.tail = None
        self.length = 0

    # Add an element to the end of the linked list
    def append(self, value): 
        node = Node(value)
        if self.head == None: 
            self.head = node
            self.tail = node
        else: 
            self.tail.next = node
            self.tail = node
        self.length += 1

    # Add an element to the beginning of the linked list
    def prepend(self, value): 
        node = Node(value)
        if self.head == None: 
            self.head = node
            self.tail = node
        else: 
            node.next = self.head
            self.head = node
        self.length += 1
    
    # print the elements of the Linked List
    def __str__(self): 
        temp_node = self.head
        result = ""

        while temp_node is not None: 
            result += str(temp_node.value)
            if temp_node.next is not None: 
                result += "->"
            temp_node = temp_node.next

        return result


linkedlist = LinkedList()
linkedlist.append(10)
linkedlist.append(20)
linkedlist.append(30)
linkedlist.prepend(5)
print(linkedlist.length)
print(linkedlist)

