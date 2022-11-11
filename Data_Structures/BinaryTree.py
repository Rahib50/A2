#Binary tree is a data structure where each node is allowed ro have two child nodes
#In this case it is a Binary search tree
#A starting number is taken
#If the next number is greater, it is right child. IF NOT then left child
#This Binary search tree is heavily reliant on Recursion so it's capability may be limited depending on the spec of the computer

class tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.count = 1
    
    #Method to get values into Forever branching tree
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left == None:
                    self.left = tree(data)
                
                else: self.left.insert(data)
            
            else:
                if self.right == None:
                    self.right = tree(data)
                
                else: self.right.insert(data)
            
        else:
            self.data = data 
        self.count += 1
    
    #Method to found total number of elements in the tree
    def total(self):
        return self.count
    
    #Method to indicate presence of searched item
    def search(self, item):
        if item < self.data:
            if self.left is None: return "Item not found" #Base case declaration
            return self.left.search(item)
        
        if item > self.data:
            if self.right is None: return "Item not found" #Same base case
            return self.right.search(item)
        
        else: return "data not found"

    #print method to return all elements from leftmost to rightmost
    def print_tree(self):
        if self.left:   self.left.print_tree()
        print(self.data) #Re-iterated task
        if self.right: self.right.print_tree()

MyTree = tree(12)
MyTree.insert(5)
MyTree.insert(90)
MyTree.insert(88)    
MyTree.insert(6)
MyTree.insert(0)
MyTree.insert(12)
MyTree.insert(11)
print(MyTree.total())
MyTree.print_tree()

