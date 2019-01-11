# This is a singly linked list using a Node class that has more links available to it than this list needs.
# This linked list was originally written with only a tail-insert function.
# Written by Robert De La Cruz II on Dec 30, 2018 for the purpose of self-edification
# Sources looked into include StackOverflow, https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/ and https://www.w3schools.com/python/default.asp
# Last edited Jan 11, 2019

from Node import Node


class SinglyLinkedList_NODE:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        return

    # Get number of nodes in the list
    def get_size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_link0()
        return count

    # Search the list
    def search(data):
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

    # Remove the first occurance of an item from the list
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
        return

    # This is a head-insert
    def headIns(self, data):
        newNode = Node(data)
        if self.head is None:
            self.tail = self.head = newNode
        else:
            newNode.set_link0(self.head)
            self.head = newNode
        return

    # This is a tail-insert
    def tailIns(self, data):
        newNode = Node(data)
        if self.head is None:
            self.tail = self.head = newNode
        else:
            self.tail.set_link0(newNode)
        self.tail = newNode
        return

    # Print the list from the head
    def printList(self):
        current = self.head
        print('\nPrinting the list:')
        while current is not None:
            print(current.get_data())
            current = current.get_link0()
        return

