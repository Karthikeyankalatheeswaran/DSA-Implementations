class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
        
    def enqueue(self,value):
        newNode = Node(value)
        if self.length == 0 :
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
        self.length +=1
        return self 
    
    def dequeue(self):
        if not self.front:
            return None
        self.front = self.front.next
        self.length -=1
        return self
    
    def peek(self):
        return self.front
    
    def printQueue(self):
        current = self.front
        elements = []
        while current:
            elements.append(current.value)
            current = current.next
        print("Queue:", " -> ".join(map(str, elements)))
    
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.printQueue()  # Output: Queue: 10 -> 20 -> 30
print("Dequeued:", q.dequeue())  # Output: Dequeued: 10
q.printQueue()  # Output: Queue: 20 -> 30
print("Front:", q.peek())  