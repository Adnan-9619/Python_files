class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self): 
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(f"{current.data}->")
            current = current.next
        print("None")


adnan = Linkedlist()
adnan.append(1)
adnan.append(2)
adnan.append(1)
adnan.print_list()

a = [1, 2, 4, 5, 6, 8]
l1 = []


def checked():
    for i in range(5, -1, -1):
        l1.append(a[i])

    print(l1)


checked()
