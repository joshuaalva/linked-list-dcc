# ---------------------------------------------------------------------------------------------------------------
# Node class
# lets get started by creating a Node class. Each Node object consist of data element and a pointer
# The Node class specifies member variables for the data and the pointer 

# Code for the node class
class Node():
    def __init__(self, data): 
        self.data = data 
        self.next = None

# The Node class has two member variables: self.data, a string, and self.next, a pointer to the next node of the list 
# The self.next variable should contain only another Node object, or if empty the void value None. 

# The constructor initializes a Node object with one input parameter, and the self.next variable is set to None 

# ---------------------------------------------------------------------------------------------------------------
# The Linked List Class 

# The LinkedList class creates a pointer to the head of the list and initially sets it to None
# The LinkedList class will also include methods that manipulate the linked list. 

# Code for the LinkedList class

# from node import Node
# class LinkedList():
#     def __init__(self):
#         self.head = None

# In the LinkedList class, the self.head variable is a pointer to the head of the list. The self.head pointer is initially set to None because the list is empty

# ---------------------------------------------------------------------------------------------------------------
# The append() Method

# A linked list is populated by appending elements, such as "Sa", "Re", and "Ga", to the end of the data structure. 
# When this list is empty, the element being appended becomes the head of the list. 
# Otherwise a loop traverses the list to the last element where you can append the new node. 
# To populate the linked list class(), you create the append() method. 

# Sudo code for the algorithm of append goes like this 
# create an instance of a node that contains the data to append 
# if the linked list is empty: 
    # set the start of the linked list to the new code 
# Otherwise: 
    # create a searcher pointer that starts at the head of the linked list 
    # while the searcher pointer does not point to the end of the list: 
    # advance the searcher pointer to the next node 
    # at the end of the list, set the last pointer to reference the same node as the new node pointer so that the new node is linked to the list

# how can you tell if a list is empty? 
# the head points to None 

# Code for appending a new element to the end of a linked list 

# from node import Node 
# class LinkedList(): 
#     def __init__(self):
#         self.head = None
#     def append(self, data): 
#         new_node = Node(data)
#         if self.head == None: 
#             self.head = new_node
#         else: 
#             searcher = self.head 
#             while searcher.next != None: 
#                 searcher = searcher.next 
#             searcher.next = new_node 

# the append() method begins with new_node = Node(data), which creates a new node containing a data value and an associated variable called new_node 

# from linkedList import LinkedList 
# my_list = LinkedList()
# my_list.append("Sa")
# my_list.append("Re")
# my_list.append("Ga")

# driver code to append elements to a linked list 

#---------------------------------------------------------------------------------------------------------------
# The prepend() Method

# Used to add data to the beginning of a linked list class, you create the prepend() method 

# ---------------------------------------------------------------------------------------------------------------
# Finding an element in a Linked List 
# In Python you can use the keyword, in to detect if an object contains a value
# The statement 5 in [1, 2, 3, 4, 5] returns True 

# from node import Node 
# class LinkedList(): 
#     def __init__(self):
#         self.head = None
#     def __str__(self): 
#         # Omitted 
#     def __contains__(self, target): 
#         traverser = self.head 
#         while traverser != None: 
#             if traverser.data == target:
#                 return True 
#             traverser = traverser.next
#         return False 
#     def prepend(self, data):
#         #Omitted
#     def append(self, data): 
        # Omitted 

#---------------------------------------------------------------------------------------------------------------
# The insert() Method 

# Inserting an element into a linked list requires you to shuffle pointers. The general pseudo code for the algorithm is: 
# start a temporary pointer varialbe at the front of the linked list 
# walk the pointer to the location to insert the new element by advancing the pointer to the next node 
# create a new node with the new data and have its next pointer point to the temporary variable's next 
# point the temporary variables next to the new node 









