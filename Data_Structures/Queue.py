#The data structure Queue is pretty similar to Stack but follows the FIFO principle
class Queue:
    def __init__(self):
        self.queue = list()

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) > 0:
            self.queue.pop(0)
    
    def print_queue(self):
        print(self.queue)
    
    def queue_len(self):
        return len(self.queue)

aqueue = Queue()

#enqueue testing
for i in range(3):
    a = input("Enter something to push to Queue: ")
    aqueue.enqueue(a)

aqueue.print_queue()

#Dequeue testing
while aqueue.queue_len() > 1:
    aqueue.dequeue()
    aqueue.print_queue()