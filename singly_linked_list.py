class Node: 
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def printLL(self):
        if self.head is None:
            print("The list is empty!")
        else:
            while self.head is not None:
                print(self.head.data)
                self.head = self.head.next
    def createNode(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
    def afterNode(self,data,x):
        temp = self.head
        while temp is not None:
            if temp.data == x:
                break
            temp=temp.next
        if temp is None:
            print("The element is not at the list!")
        else:
            afterNode = Node(data)
            afterNode.next = temp.next
            temp.next = afterNode
    def beforeNode(self,data,x):
        temp = self.head
        while temp is not None:
            if temp.next.data == x:
                break
            temp = temp.next
        if temp is None:
            print("The given element is not in the list!")
        else:
            beforeNode = Node(data)
            beforeNode.next = temp.next
            temp.next = beforeNode
    def add_end(self,data):
        end_node = Node(data)
        
        if self.head is None:
            self.head = end_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = end_node


LL = LinkedList()
LL.createNode(10)
LL.createNode(20)
LL.createNode(30)
LL.afterNode(25,20)
LL.beforeNode(15,20)
LL.add_end(50)
LL.printLL()
