class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
#Traverse and Print
    def printLL(self):
        n = self.head
        while n is not None:
            print(n.data)
            n = n.next
#Adding new data at beginning
    def add_begins(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node
#ADDING DATA AT THE END
    def add_end(self,data):
        end_node = node(data)
        
        if self.head is None:
            self.head = end_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = end_node

#ADDING AFTER A SPECIFIC NODE
    def add_after(self,data,x):
        temp = self.head
        while temp is not None:
            if x == temp.data:
                break
            temp = temp.next
        if temp is None:
            print("The node is not present is the LinkedList!")
        else:
            after_node = node(data)
            after_node.next = temp.next
            temp.next = after_node

#ADDING BEFORE THE SPECIFIC NODE
    def add_before(self,data,x):
        if self.head.data == x:
            before_node = node(data)
            before_node.next = self.head
            self.head = before_node
        else:
            temp = self.head
            while temp.next is not None:
                if temp.next.data == x:
                    break
                temp = temp.next
                
            if temp.next is None:
                print("The given node is not present")
            else:
                before_node = node(data)
                before_node.next = temp.next
                temp.next = before_node
            



LL1 = linkedList()
LL1.add_begins(10)
LL1.add_end(20)
LL1.add_end(30)
LL1.add_end(40)
LL1.add_after(50,30)
LL1.add_before(60,40)
LL1.printLL()