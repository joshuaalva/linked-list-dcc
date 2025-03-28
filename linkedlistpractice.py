class node: 
    def __init__(self, data = None):
        self.data = data
        self.next = None 

# Linked List class wraps over the nodes 

class linked_list:
    def __init__(self): 
        self.head = node()
        # used as a place holder 
    def append(self, data): 
        # append function
        new_node = node(data)
        current = self.head
        #iterate over each one of the nodes 
        while current.next != None: 
            current = current.next 
        current.next = new_node
    def length(self):
        current = self.head 
        total = 0 
        while current.next != None: 
            total += 1 
            current = current.next 
        return total 
    def display(self): 
        elements = []
        current_node = self.head
        while current_node.next != None: 
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)
    def get(self, index):
        if index >= self.length():
            print("Error: 'get' index out of range!")
            return None 
        current_index = 0
        current_node= self.head
        while True: 
            current_node = current_node.next
            if current_index == index: 
                return current_node.data
            current_index += 1
                

my_list = linked_list()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()

print(my_list)
print(f"Element at 2nd index: {my_list.get(2)}")
