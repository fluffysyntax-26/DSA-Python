class Node: 
    def __init__(self, value): 
        self.value = value
        self.next = None

class LinkedList: 
    def __init__(self): 
        self.head = None
        self.tail = None
        self.length = 0

    # add element at end O(1) - constant time complexity
    def append(self, value): 
        node = Node(value)

        if self.head == None: 
            self.head = node
            self.tail = node
        else: 
            self.tail.next = node
            self.tail = node

        self.length += 1

    # add element at the beginning O(1) - constant time complexity
    def prepend(self, value): 
        new_node = Node(value)

        if self.head == None: 
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.next = self.head
            self.head = new_node

        self.length += 1

    # insert at a specific index 0(n) - linear time complexity
    def insert(self, value, index): 
        new_node = Node(value)

        # error handling for index out of bounds
        if index < 0 or index > self.length: 
            raise ValueError ("Index out of Bounds")

        # insert at head
        if index == 0: 
            new_node.next = self.head
            self.head = new_node
            if self.length == 0: 
                self.tail = new_node
            self.length += 1
            return 
        
        # insert other than head
        temp_node = self.head
        for _ in range(index-1): 
            temp_node = temp_node.next
    
        new_node.next = temp_node.next
        temp_node.next = new_node

        self.length += 1

    # print elements of the linked list
    def __str__(self):
        temp_node = self.head
        result = " "
        while temp_node is not None: 
            result += str(temp_node.value)
            if temp_node.next is not None: 
                result += "->"
            temp_node = temp_node.next
        
        return result
    
    # loop through all elements in a linked list
    def traverse(self): 
        current = self.head
        while current is not None: 
            print(current.value)
            current = current.next

    # search using key 
    def search(self, value): 
        current = self.head
        index = 0
        while current is not None: 
            if current.value == value:
                return f"Element found at index {index}"
            current = current.next
            index += 1
        
        return "Element not found"
    
    # search using index
    def get(self, index): 
        if index < 0 or index > self.length: 
            raise ValueError("Index Out of Bounds")
        
        if index == self.length-1: 
            return self.tail
        
        current = self.head
        for _ in range(index): 
            current = current.next
        return current
    
    # update using index
    def set(self, value, index): 
        temp = self.get(index)
        if temp is not None: 
            temp.value = value
            return "Element Set Successfully"
        return "Could not change Element Value"

    # remove first node and return
    def pop_first(self): 
        if self.length == 0: 
            return None
        
        popped_node = self.head
        if self.length == 1: 
            self.head = None
            self.tail = None
            return popped_node
        else: 
            self.head = self.head.next
            popped_node.next = None

        self.length -= 1
        return popped_node.value

    # remove last node and return
    def pop(self): 
        if self.length == 0: 
            return None
        
        popped_node = self.tail

        if self.length == 1: 
            self.head = None
            self.tail = None
            return popped_node
        
        else: 
            temp = self.head
            while temp.next is not self.tail: 
                temp = temp.next
                
            self.tail = temp
            temp.next = None
            self.length -= 1

        return popped_node
    
    # remove using index
    def remove(self, index): 
        current = self.head
        for _ in range(index): 
            current = current.next

        current.next = current.next.next
        del current


    
ll = LinkedList()
ll.append(20)
ll.append(30)
ll.prepend(10)
print(ll)
ll.insert(15, 1)
print(ll)

ll.insert(5, 0)
print(ll)


print(ll.search(5))
print(ll.get(4))

print(ll.set(14, 2))
print(ll)

print(ll.pop_first())
print(ll.pop().value)
