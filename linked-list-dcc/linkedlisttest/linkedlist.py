from main import fName, pNumber, dateOfBirth, newCustomer

class Node(): 
    def __init__(self, data): 
        self.data = data 
        self.next = None

class LinkedList(): 
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head == None: 
            self.head = new_node 
        else: 
            searcher = self.head 
            while searcher.next != None: 
                searche = searcher.next 
            searcher.next = new_node
    
    def __str__(self):
        string = ""
        if self.head == None:
            string += "The list is empty"
        else: 
            traverser = self.head 
            while traverser != None:
                traverser = traverser.next
        return string
    
    def __contains__(self, target):
        traverser = self.head
        while traverser != None:
            if traverser.data == target:
                return True
            traverser = traverser.next 
        return False
    
    # def prepend(self, data):
    #     new_node = Node(data)
    #     new_node.next = self.head
    #     self.head = new_node 
