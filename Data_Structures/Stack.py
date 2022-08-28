#A stack is where LIFO principle is used
class Stack:
    def __init__(self):
        self.stack = list()
    
    def push(self, data):
        if data not in self.stack: #This is to keep all elements unique
            self.stack.append(data)
            return True
        
        else: return False
    
    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()
        else:
            return "Stack is empty!"

    def stack_len(self):
        return len(self.stack)

    def print_stack(self):
        print(self.stack)

#Testing
astack = Stack()
astack.push("Berry") #pushing random stuff in
print(astack.push("Berry"))
astack.push("cherry")
astack.push("apple")

astack.print_stack()

while astack.stack_len() > 1:
    astack.pop()
    astack.print_stack()


