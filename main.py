# This is test code for the various basic data structures being written for self edification.
# Written by Robert De La Cruz II
# Written on Jan 10, 2019
# Last edited Jan 10, 2019

import SinglyLinkedList_NODE as SLL
import DoublyLinkedList_NODE as DLL

# Singly Linked List tests
def sll_tests():
    datadump = []
    for i in range(100):
        list1 = SLL.headIns(i)
        list2 = SLL.tailIns(i)
    list1.printList_HEAD()
    list2.printList_TAIL()

# Doubly Linked List tests
def dll_tests():
    datadump = []
    for i in range(100):
        list1 = DLL.headIns(i)
        list2 - DLL.tailIns(i)
    list1.printList()
    list2.printList()

print('Hello from main!')
print('Would you like to:\n')
print('(1) Run the Singly Linked List tests\n')
print('(2) Run the Doubly Linked List tests\n')
choice = input('Your choice? ')
if choice == '1':
    sll_tests()
if choice == '2':
    dll_tests()
else:
    print('Not a correct choice. Please rerun to try again..')
