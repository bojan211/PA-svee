import sys
from class_example import Data, Node, Tree

import random
import time





def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list







def addLeft(nodParrent, nodChild):
    nodParrent.left = nodChild
    nodChild.parrent = nodParrent

def addRight(nodParrent, nodChild):
    nodParrent.right = nodChild
    nodChild.parrent = nodParrent

def InorderTreeWalk(x):
    if x != None:
        InorderTreeWalk(x.left)
        print(x.data.a1)
        #print(x.left.data.a1)
        InorderTreeWalk(x.right)


def TreeSearch(x,key):
    if x == None or key == x.data.a1:
        print(x.data.a1,x.data.a2)
        return x
        
    if key < x.data.a1:
        TreeSearch(x.left, key)
    else:
        TreeSearch(x.right, key)
        

def IterativeTreeSearch(x,key):
    while x != None and key != x.data.a1:
        if key < x.data.a1:
            x = x.left
        else:
            x = x.right

    print(x.data.a1,x.data.a2)
    return x

def TreeMin(x):
    while x.left != None:
        x = x.left
        
    #print("MIN JE : ",x.data.a1, x.data.a2)
    return x            


def TreeMax(x):
     while x.right != None:
        x = x.right
        
     
     return x 

def TreeSuccessor(x):
    if x.right != None:
       return TreeMin(x.right)
    y = x.parrent
    while y!=None and x==y.right:
        x = y
        y = y.parrent
    return y

def TreeInsert(t,z):
    y = None
    x = t
    while x != None:
        y = x
        if z.data.a1 < x.data.a1:
            x = x.left
        else:
            x = x.right
    z.parrent = y
    if y == None:
        t = z
        print("AAAAA")
    elif z.data.a1 < y.data.a1:
        y.left = z
    else:
        y.right = z


def Transplant(t,u,v):
    if u.parrent == None:
        t = v
    elif u == u.parrent.left:
        y.parrent.left = v
    else:
        u.parrent.right = v
    if v == None:
        v.parrent = u.parrent


def TreeDelete(t,z):
    if z.left == None:
        Transplant(t,z,z.right)
    elif z.right == None:
        Transplant(t,z,z.left)
    else:
        y = TreeMinimum(z.right)
        if y.parrent != z:
            Transplant(t,y,y.right)
            y.right = z.right
            y.right.parrent = y
        Transplant(t,z,y)
        y.left = z.left
        y.left.parrent = y

    

if __name__ == "__main__":
    
    d1 = Data(2, "2")
    d2 = Data(6, "6")
    d3 = Data(3, "3")
    d4 = Data(8, "8")
    d5 = Data(1, "1")
    d6 = Data(5, "5")
    d7 = Data(4, "4")

    n1 = Node(d = d1)
    n2 = Node(d = d2)
    n3 = Node(d = d3)
    n4 = Node(d = d4)
    n5 = Node(d = d5)
    n6 = Node(d = d6)
    n7 = Node(d = d7)
    n8 = Node(d = Data(7, "7"))

    addLeft(n2, n1)   #6,2
    addRight(n1,n3)   #2,3
    addRight(n2,n4)   #6,8
    addLeft(n1,n5)    #2,1
    addRight(n3,n6)   #3,5
    addLeft(n6,n7)    #5,4

    InorderTreeWalk(n2)

    TreeSearch(n2, 5)
    IterativeTreeSearch(n2,6)

    m = TreeMin(n2)
    print("MIN JE : ",m.data.a1, m.data.a2)
    m = TreeMax(n2)
    print("MAX JE : ",m.data.a1, m.data.a2)
    m = TreeSuccessor(n3)
    print("Sledeci najveci je : ",m.data.a1, m.data.a2)

    print("Ubacivanje sedmice:")
    TreeInsert(n2,n8)
    InorderTreeWalk(n2)
    print("Posle brisanja trojke")
    TreeDelete(n2,n3)
    InorderTreeWalk(n2)

    T = Tree(None)
    

    l = random_list(1, 100, 20)

    for i in range(len(l)):
        n = Node(d = Data(l[i],"A"))
   
        T.TreeInsert( n);
        print(T.root)

    print("NOVO")
    InorderTreeWalk(T.root)

    