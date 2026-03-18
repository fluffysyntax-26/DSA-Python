class Node: 
    def __init__(self, value): 
        self.value = value
        self.next = None

class LinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value): 
        new_node = Node(value)
        if self.head is None: 
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value): 
        new_node = Node(value)
        if self.head is None: 
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, value, index): 
        new_node = Node(value)
        if index < 0 or index > self.length: 
            raise IndexError("Index out of Bounds")
        
        # insert at head
        if index == 0: 
            new_node.next = self.head
            self.head = new_node
            if self.length == 0: 
                self.tail = new_node
            self.length += 1
            return
        
        # insert other than head
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.length += 1
        
    def traverse(self): 
        current = self.head
        items = []
        while current is not None: 
            items.append(current.value)
            current = current.next
        return items

    # Search using key 
    def search(self, key):
        current = self.head
        index = 0
        while current is not None: 
            if current.value == key: 
                return f"Element Found at Index {index}"
            current = current.next
            index += 1
        return "Element does not exist"

    # search using index
    def get(self, index): 
        if index < 0 or index > self.length: 
            raise IndexError("Index out of Bounds")
        
        if index == 0: 
            return self.head.value
        
        if index == self.length: 
            return self.tail.value
        
        current = self.head
        for _ in range(index): 
            current = current.next
        return current.value

    # update at index
    def set(self, index, value): 
        if index < 0 or index >= self.length: 
            raise IndexError("Index out of bounds")
        
        if index == 0: 
            self.head.value = value
        
        current = self.head
        for _ in range(index): 
            current = current.next
        current.value = value
    
    # delete at position
    def delete(self, index): 
        if index < 0 or index >= self.length: 
            raise IndexError("Index Out of Bounds")
        
        if index == 0: 
            self.head = self.head.next
            if self.length == 1: 
                self.tail = None
            self.length -= 1
            return
        
        prev = self.head
        for _ in range(index-1):
            prev = prev.next
        target = prev.next
        prev.next = target.next
        
        # if deleted the last node, update the tail
        if index == self.length - 1: 
            self.tail = prev
        self.length -= 1

    # delete linkedlist entire linkedlist
    def obliterate(self): 
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        result = ""
        current = self.head
        while current is not None: 
            result += str(current.value)
            if current.next is not None: 
                result += "->"
            current = current.next
        return result

    def __len__(self):
        return self.length

linkedlist = LinkedList()

nums = [x*10 for x in range(1,11)]
print("List:\n", nums)

print("Linked List: ")
linkedlist.prepend(5)
for num in nums: 
    linkedlist.append(num)
linkedlist.insert(15, 2)
print(linkedlist)

print("Length of Linked List:", len(linkedlist))
print("Linked Items (Traverse):", linkedlist.traverse())
print(linkedlist.search(80))
print(linkedlist.get(12))
print(linkedlist.set(2, 18))
print(linkedlist)