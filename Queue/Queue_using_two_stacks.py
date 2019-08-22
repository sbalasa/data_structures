from .Stack import Stack


class Queue:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()
 
    def is_empty(self):
        return (self.inbox.is_empty() and self.outbox.is_empty())
    
    def size(self):
        return self.inbox.size()
    
    def clear(self):
        self.inbox = Stack()
        self.outbox = Stack()
    
    def display(self):
        self.inbox.display()
 
    def enqueue(self, data):
        self.inbox.push(data)
 
    def dequeue(self):
        if self.outbox.is_empty():
            while not self.inbox.is_empty():
                popped = self.inbox.pop()
                self.outbox.push(popped)
        return self.outbox.pop()


if __name__ == "__main__":
    q = Queue()
    q.enqueue(4)
    q.enqueue(5)
    q.clear()
    q.enqueue(17)
    q.enqueue(1)
    q.display()
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
