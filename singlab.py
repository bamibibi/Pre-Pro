class DataNode:
    def __init__(self, input_name=""):
        self.name = input_name
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None
    def traverse(self):
        if self.head is None:
            print("This is an empty list.")
        else:
            pos = self.head
            while pos is not None:
                print("->", pos.name, end=" ")
                pos = pos.next
            print("")

    def insertFront(self, data):
        pNew = DataNode(data)
        if self.head is None:
            self.head = pNew
        else:
            pNew.next = self.head
            self.head = pNew
        self.count += 1

    def insertLast(self, data):
        pNew = DataNode(data)
        if self.head is None:
            self.head = pNew
        else:
            pos = self.head
            while pos.next is not None:
                pos = pos.next
            pos.next = pNew

    def insertBefore(self, node, data):
        pNew = DataNode(data)        
        if self.head is None:
            self.head = pNew
        else:
            pos = self.head
            while True:
                if pos.next.name != node:
                    pos = pos.next
                else:
                    pNew.next = pos.next              
                    pos.next = pNew                    
                    break
    def deletenode(self, node):
        pos = self.head
        while True:
                if pos.next.name != node:
                    pos = pos.next
                else:
                    pos.next = pos.next.next
                    break

mylist = SinglyLinkedList()
pNew = DataNode("Hiw")
mylist.head = pNew
pNew = DataNode("Khao")
mylist.head.next = pNew
pNew = DataNode("Mak")
mylist.head.next.next = pNew

mylist.insertFront("Bam")
mylist.traverse()
mylist.insertLast("Tsud")
mylist.traverse()
mylist.insertBefore("Hiw", "bibi")
mylist.traverse()
mylist.deletenode("Mak")
mylist.traverse()