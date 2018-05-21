class Node:
    """
    Tree node: left child, right child and data
    """
    def __init__(self, l = None, r = None, d = None, p = None):
        """
        Node constructor 
        @param A node data object
        """
        self.left = l
        self.right = r
        self.data = d
        self.parrent = p

class Data:
    """
    Tree data: Any object which is used as a tree node data
    """
    def __init__(self, val1, val2):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.a1 = val1
        self.a2 = val2

class Tree:

    def __init__(self, val1):
        
        self.root = val1

    def TreeInsert(self,z):
        y = None
        x = self.root
        while x != None:
            y = x
            if z.data.a1 < x.data.a1:
                x = x.left
            else:
                x = x.right
        z.parrent = y
        if y == None:
            self.root = z
            print("AAAAA")
        elif z.data.a1 < y.data.a1:
            y.left = z
        else:
            y.right = z

d = Data(1, 2)
#print(d.a1, d.a2)