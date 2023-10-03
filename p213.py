#982

'''
Python program to reverse a linked list
'''

class Node:
    # constructor to initialize the node object
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    #Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    #Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    #utility function to print the linkedList
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end = " ")
            temp = temp.next

llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

print("Given Linked List")
llist.printList()
llist.reverse()
print("\nReversed Linked List")
llist.printList()

####################################################################################################################

#983

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

Class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    def reverseUtil(self, curr, prev):
        if curr.next is None:
            self.head = curr

            # Update next to prev node
            curr.next = prev
            return

        # Save curr.next node for recursive call
        next = curr.next

        # And update next
        curr.next = prev

        self.reverseUtil(next,curr)

    # This function mainly calls reverseUtil() with previous as None
    def reverse(self):
        if self.head is None:
            return
        self.reverseUtil(self.head,None)

    # Function to insert a new mode at the beginning
    def push(self, new_data):
        new_mode = Node(new_data)
        new_node.next = self.head
        self.head = new_mode

    # Utility function to print the LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next

#Driver program
llist = LinkedList()

llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print("GIven linked list")
llist.printList()

llist.reverse()

print("\nReverse linked list")
llist.printList()

######################################################################################################################
