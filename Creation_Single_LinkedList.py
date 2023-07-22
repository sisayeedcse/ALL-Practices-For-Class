class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Single_LinkedList:
    def __init__(self):
        self.head = None
    def printSLL(self):
        temp = self.head
        if temp is None:
            print("List is empty!")
        else:
            while temp is not None:
                print(temp.data)
                temp = temp.next
    def new_node(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode
        

L = Single_LinkedList()
L.new_node(10)
L.new_node(20)
L.new_node(30)
L.new_node(40)

L.printSLL()