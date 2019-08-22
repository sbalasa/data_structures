class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def dequeue(self):
        if not self.head:
            return "Queue is Empty"
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            data = temp.data
            size = self.size() - 2
            temp = self.head
            try:
                while size:
                    size -= 1
                    temp = temp.next
                temp.next = None
                return data
            except AttributeError:
                self.head = None

    def display(self):
        if not self.head:
            return "Queue is Empty"
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print("\n")

    def size(self):
        count = 0
        temp = self.head
        while temp:
            temp = temp.next
            count += 1
        return count
    
    def is_empty(self):
        size = self.size()
        return False if size else True

    def search(self, data):
        if not self.head:
            print(-1)
        else:
            index = 0
            temp = self.head
            try:
                while temp.data != data:
                    index += 1
                    temp = temp.next
                print(index)
            except AttributeError:
                print(-1)

    def get_data(self, pos):
        temp = self.head
        count = 0
        try:
            while count != pos:
                temp = temp.next
                count += 1
            print(temp.data)
        except AttributeError:
            print(-1)

    def clear(self):
        self.head = None


if __name__ == "__main__":
    q = Queue()
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(7)
    q.display()
    print(q.dequeue())
    q.get_data(pos=1)
    q.display()
    q.clear()
    q.enqueue(19)
    q.enqueue(11)
    q.enqueue(1)
    q.enqueue(7)
    q.enqueue(4)
    q.display()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.display()
