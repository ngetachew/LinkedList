

class Node:

    def __init__(self, v : int, p):
        self.value = v
        self.pointer = p

class LinkedList:
    #Data values are ints
    def __init__(self, h):
        self.head = Node(h, None)

    def create_node(self):
        return Node(0, None)

    def add_node(self, val):
        temp =  self.create_node()
        p = None
        temp.value = val
        if self.head == None:
            self.head = temp
        else:
            p = self.head
            while (p.pointer != None):
                p = p.pointer
            p.pointer = temp
   
    def print_list(self):
        nd = self.head
        while( nd != None):
            print(str(nd.value) + '--> \n')
            nd = nd.pointer
        

#Implementation

link_lst = LinkedList(2)
link_lst.add_node(2)
link_lst.add_node(4)
link_lst.add_node(21231)
link_lst.print_list()

