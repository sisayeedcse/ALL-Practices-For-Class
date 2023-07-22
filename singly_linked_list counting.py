class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def printLinkedList(self):
        temp = self.head
        if temp is None:
            print("This list is empty!")
        else:
            while temp is not None:
                print(temp.data)
                temp = temp.next
# New Node one by one
    def new_node(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
#Counting the elements 
    def count(self):
        flag = 0 # declare a variable init. value to  0
        temp = self.head 
        while temp is not None:
            temp = temp.next #traverse till None
            flag = flag + 1 #variable flag increment
        print("Total element number is - ", flag) #printing the flag variable

LL = LinkedList()
LL.new_node(10)
LL.new_node(20)
LL.new_node(30)
LL.new_node(40)
LL.printLinkedList()
LL.count() #calling the count function after the nodes creation