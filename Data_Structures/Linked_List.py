#Linked list is a data structure where each item points to the next item in the list.
#In a linked list a new element is always added at the start of the list

class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None
    
    def print_LinkedList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

a = linked_list()
a.head = node("Apple")
second = node("Karim")
third = node("James")
a.head.next = second
second.next = third

a.print_LinkedList()