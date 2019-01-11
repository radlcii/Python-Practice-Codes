# This is test code for the various basic data structures being written for self edification.
# Written by Robert De La Cruz II
# Written on Jan 10, 2019
# Last edited Jan 10, 2019

# Singly Linked List tests
def sll_tests():
    from SinglyLinkedList_NODE import SinglyLinkedList_NODE
    list1 = SinglyLinkedList_NODE()
    list2 = SinglyLinkedList_NODE()
    for i in range(1, 11):
        list1.headIns(i)
        list2.tailIns(i)
    list1.printList()
    list2.printList()

# Doubly Linked List tests
def dll_tests():
    from DoublyLinkedList_NODE import DoublyLinkedList_NODE
    list1 = DoublyLinkedList_NODE()
    list2 = DoublyLinkedList_NODE()
    for i in range(1, 11):
        list1.headIns(i)
        list2.tailIns(i)
    list1.printList()
    list2.printList()

print('Hello from main!')
print("""'Would you like to:
(1) Run the Singly Linked List tests
(2) Run the Doubly Linked List tests""")

choice = input('Your choice? ')
if choice == '1':
    sll_tests()
elif choice == '2':
    dll_tests()
else:
    print('Not a valid choice. Please rerun to try again.')

print('\nTest finished, exiting program.')
