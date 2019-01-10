# This is test code for the various basic data structures being written for self edification.
# Written by Robert De La Cruz II
# Written on Jan 10, 2019
# Last edited Jan 10, 2019

import SinglyLinkedList as SLL
import DoublyLinkedList as DLL


class tester:
    def init_(self):
        print('Would you like to:\n')
        print('(1) Run the Singly Linked List tests\n')
        print('(2) Run the Doubly Linked List tests\n')
        input('Your choice?', choice)
    if choice is 1:
        sll_tests()
    if choice is 2:
        dll_tests()
    else:
        print('Not a correct choice. Please rerun to try again..')

    def sll_tests(self):
        datadump = []
        for i in 100:
            list1 = SLL.headIns(i)
            list2 = SLL.tailIns(i)
        list1.printList_HEAD()
        list2.printList_TAIL()

    def dll_tests(self):
        datadump = []
        for i in 100:
            list1 = DLL.headIns(i)
            list2 - DLL.tailIns(i)
        list1.printList()
        list2.printList()
                