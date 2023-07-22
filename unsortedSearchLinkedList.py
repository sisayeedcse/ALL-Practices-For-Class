class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def printLL(self):
        if self.head is None:
            print("List is empty!")
        else:
            temp = self.head
            print("The linked list is: ")
            while temp is not None:
                print(temp.data , end=" ")
                temp = temp.next
    def newNode(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
    def Unsort_search(self,ITEM):
        ptr = self.head
        pos = 1
        while ptr is not None:
            if ptr.data == ITEM:
                print("The item is found at LOC- ", pos)
                break
            else:
                ptr = ptr.next
                pos = pos + 1
        if ptr is None:
            print("The ITEM is not found")


LL = LinkedList()
LL.newNode(15)
LL.newNode(45)
LL.newNode(85)
LL.newNode(55)
LL.newNode(30)
LL.newNode(20)
LL.Unsort_search(55)
LL.printLL()