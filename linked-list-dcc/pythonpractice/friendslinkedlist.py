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
                searcher = searcher.next 
            searcher.next = new_node

    def __str__(self): 
        value = []
        curr = self.head
        while curr: 
            print(curr.data, end=" -> ")
            curr = curr.next
        value.append("No more friends left")
        return "->".join(value)
 

    

mylist = LinkedList()
mylist.append("Lizzie")
mylist.append("Mike")
mylist.append("Tyler")

print(mylist)