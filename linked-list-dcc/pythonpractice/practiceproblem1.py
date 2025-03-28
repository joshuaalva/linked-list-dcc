# write a python program to create a singly linked list, append some items and iterate through the list 

# step one create a new node 
class node(): 
    def __init__(self, data): 
        self.data = data 
        self.next = None 

# create the linked list 
class linked_list: 
    def __init__(self): 
        self.head = None

    def append(self, data): 
        new_node = node(data)
        if not self.head: 
            self.head = new_node 
            return 
        last = self.head
        while last.next: 
            last = last.next
        last.next = new_node 
    
    def print_list(self): 
        current = self.head
        while current: 
            print(current.data, end=" -> ")
            current = current.next 
        print("None")

list = linked_list()
list.append(10)
list.append(20)
list.append(30)

list.print_list()  # Output: 10 -> 20 -> 30 -> None
