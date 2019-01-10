# This is a doubly linked list using a modular Node class.
# Written by Robert De La Cruz II on Jan 10, 2019 for self-edification.

import Node  # Node class should be in the same directory


class DoublyLinkedList:
    def_init(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    # Tail insert function
    def tailIns(self, data):
        newNode = Node(data)
        if head is None:
            head = newNode
            tail = head
        else:
            newNode.set_link1(tail)
            tail.set_link0(newNode)
            tail = tail.link0
            head.set_link1(tail)

    # Head insert function
    def headIns(self, data):
        newNode = Node(data)
        newNode.set_link1(tail)
        newNode.set_link0(head)
        head = newNode

    # Get size copied from Singly Linked List
    def get_size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_link0()
        return count

    # Head search copied from Singly Linked List
    def headSearch(self, data):
        current = self.head
        found = False
        while current is not tail and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_link0()
        if current is None:
            return None
        return current

    # Tail search function
    def tailSearch(self, data):
        current = self.tail
        found = False
        while current is not head and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_link1()
            if current is None:
                return None
        return current

    # Search from both sides at once for giggles
    def bothSearch(self, data):
        front = self.head
        back = self.tail
        while front is not tail and front.get_link0 is not tail:
            if data == front.get_data():
                return front
            if data == back.get_data():
                return back
            front = front.get_link0()
            back = back.get_link1()
        return None

    # Delete copied from Singly Linked List
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_link0()
            if current is None:
                return None
            if previous is None:
                self.head = current.get_link0()
            else:
                previous.set_link0(current.get_link0())

    # Print list function
    def printList(self)
        current = self.head
        while current is not None
            print(current.get_data())
