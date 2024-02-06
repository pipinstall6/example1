class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None

# LinkedList yaratish
linked_list = LinkedList()

# Elementlar qo'shish
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

# LinkedList-ni chiqarish
linked_list.display()  # 1 -> 2 -> 3 -> None

# Elementni o'chirish
linked_list.delete(2)

# O'zgartirilgan LinkedList-ni chiqarish
linked_list.display()  # 1 -> 3 -> None
