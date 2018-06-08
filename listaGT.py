class Node:
 
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
 
    def __str__(self):
        return str(self.data)
 
class UnidirectionalList:
 
    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None
 
    def tailadd(self, data):
        if not self.head and not self.tail:
            n = Node(data)
            self.head = n
            self.tail = n
        else:
            n = self.head
            while n.next != None:
                n = n.next
            new_node = Node(data)
            new_node.prev = n
            n.next = new_node
            self.tail = new_node
            
    def headadd(self, data):
        if not self.head and not self.tail:
            n = Node(data)
            self.head = n
            self.tail = n
        else:
            n = self.tail
            while n.prev != None:
                n = n.prev
            new_node = Node(data)
            new_node.next = n
            n.prev = new_node
            self.head = new_node
 
    def printListhead(self):
        n = self.head
        while n:
            print (n)
            n = n.next
            
    def printListtail(self):
        n = self.tail
        while n:
            print (n)
            n = n.prev
 
ll = UnidirectionalList()
ll.headadd(14)
ll.headadd("test")
ll.headadd(2.34)
ll.headadd(True)
ll.tailadd(False)
 
ll.printListhead()
