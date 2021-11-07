# Linked List

# Node class  
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked-list class
class LinkedList:
    # Function to initialize head  
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning  
    def push(self, new_data):
        new_Node = Node(new_data)
        # todo 새 노드 받아서 새 head 만들기
        if self.head is None:
            self.head = new_Node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_Node

    # Delete the first occurence of key in linked list
    def deleteNode(self, key):

        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted
        # Keep track of the previous node 'prev.next'
        while temp is not None:
            prev = temp
            temp = prev.next
            if temp.data == key:
                break

        # If key was not present in linked list
        if temp == None:
            return

        # Unlink the node from linked list
        prev.next = temp.next

        temp = None

    # Utility function to print the linked LinkedList  
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    llist = LinkedList()
    llist.push("Python")
    llist.push("Java")
    llist.push("C++")
    llist.push("C#")

    print("Created Linked List: ")
    llist.printList()

    delete_key = "C++"
    llist.deleteNode(delete_key)
    print("\nLinked List after Deletion of {:s}:".format(delete_key))
    llist.printList()
