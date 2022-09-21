#Linked list is a data structure where each item points to the next item in the list.
#In a linked list a new element is always added at the start of the list
#linked list consists of a sequence of nodes connected like chains with pointers 

class LinkedListNode:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class linked_list:
    def __init__(self, head = None):
        self.head = head
    
    def insert(self, data):
        node = LinkedListNode(data)
        if self.head is None:
            self.head = node 
            print(True) #This is to check if the insertion was successful
            return
        
        current_node = self.head
        while True:
            if current_node.next is None:
                current_node.next = node
                print(True) #This is to check if the insertion was successful
                break
            current_node = current_node.next
    
    def print_LinkedList(self):
        alist  = []
        currentNode = self.head
        while currentNode is not None:
            alist.append(currentNode.value)
            currentNode = currentNode.next
        alist.append(None) #The last element points to nothing (null pointer) that's what the none represents
        print(alist)


ll = linked_list()
for i in range(3):
    n = input("Enter element for insertion: ")
    ll.insert(n)

ll.print_LinkedList()