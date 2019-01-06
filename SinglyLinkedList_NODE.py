# This is a singly linked list using a Node class that has more links available to it than this list needs.
# This linked list was originally written with only a tail-insert function.
# Written by Robert De La Cruz II on Dec 30, 2018 for the purpose of self-edification
# Sources looked into include StackOverflow, https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/ and https://www.w3schools.com/python/default.asp

import Node  # Node class should be in the same directory as this file


class SinglyLinkedList:
    def _init_(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    # This is a tail-insert
    def tailIns(self, data):
        newNode = Node(data)
        if head is None:
            head = newNode
            tail = head
        else:
            tail.set_link0(newNode)
            tail = tail.link0

    # This is a head-insert
    def headIns(self, data):
        newNode = Node(data)
        newNode.link0 = head
        head = newNode

    def get_size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_link0()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_link0()
        if current is None:
            return None
        return current

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
