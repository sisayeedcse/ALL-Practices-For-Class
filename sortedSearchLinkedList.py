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
            print("The Sorted list is: ")
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
    def sorted_search(self,ITEM):
        ptr = self.head
        pos = 1
        while ptr is not None:
            if ptr.data > ITEM:
                print("Item is not found")
                break
            elif ptr.data == ITEM:
                print("Item is found at LOC: ",pos)
                break
            else:
                ptr = ptr.next
                pos = pos +1
                
            


LL = LinkedList()
LL.newNode(10)
LL.newNode(15)
LL.newNode(25)
LL.newNode(35)
LL.newNode(40)
LL.newNode(50)
LL.sorted_search(50)
LL.printLL()