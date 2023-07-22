class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    
    # Printing the nodes
    def printLL(self):
        if self.head is None:
            print("The list is empty!")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data)
                temp = temp.next
    
    #Creating new nodes
    def newnode(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode
    
    # Adding elements after a node
    def add_after(self,data,x):
        temp = self.head
        while temp is not None:
            if x ==  temp.data:
                break
            temp = temp.next
        if temp is None:
            print("The list element is not found")
        else:
            afterNode = Node(data)
            afterNode.next= temp.next
            temp.next = afterNode
    
    # Adding elements before a node
    def add_before(self,data,x):
        if x == self.head.data:
            beforeNode = Node(data)
            beforeNode.next = self.head
            self.head = beforeNode
        else:
            temp = self.head
            while temp is not None:
                if temp.next.data == x:
                    break
                else:
                    temp = temp.next
            if temp is None:
                print("The element is not present in the node!")
            else:
                beforeNode = Node(data)
                beforeNode.next = temp.next
                temp.next = beforeNode




LL = LinkedList()
LL.newnode(10)
LL.newnode(20)
LL.newnode(30)
LL.newnode(50)
LL.add_after(60,50)
LL.add_before(40,50)
LL.printLL()