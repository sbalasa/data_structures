class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def pop(self):
        if not self.head:
            print("Stack is Empty")
        data = self.head.data
        self.head = self.head.next
        return data

    def display(self):
        if not self.head:
            print("Stack is Empty")
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
    s = Stack()
    s.push(4)
    s.push(5)
    s.push(7)
    s.display()
    s.pop()
    s.search(5)
    s.display()
    s.get_data(1)
    s.clear()
    s.display()
