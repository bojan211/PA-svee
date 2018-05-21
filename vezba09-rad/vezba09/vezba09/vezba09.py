import sys
from math import inf


from enum import Enum	

time = 0;
krajnja_lista = list()

class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, c = None, p = None, d1 = None, d2 = None, f = None):
        """
        Vertex constructor 
        @param color, parent, auxilary data1, auxilary data2
        """
        self.list = []
        self.c = c
        self.p = p
        self.d1 = d1   
        self.dist = d2
        self.f = f


class Data:
    """
    Graph data: Any object which is used as a graph vertex data
    """
    def __init__(self, val1, val2):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.a1 = val1
        self.a2 = val2
	
class VertexColor(Enum):
        BLACK = 0
        GRAY = 127
        WHITE = 255		
		

def BFS(G,s):
    for i in G:
        i.c = VertexColor.WHITE
        i.dist = inf
        i.p = None
    s.c = VertexColor.GRAY
    s.dist = 0
    s.p = None
    Q = list()
    Q.append(s)
    while len(Q) is not 0:
        u = Q.pop(0)
        for v in u.list:
            if v.c == VertexColor.WHITE:
                v.c = VertexColor.GRAY
                v.dist = u.dist + 1
                v.p = u
                Q.append(v)
        u.c = VertexColor.BLACK

 
def Print_Path(G,s,v):
    if v == s:
        print(s.d1)
    elif v.p == None:
        print("No path from " ,s.d1, " to ",v.d1, " exist")
    else:
        Print_Path(G,s,v.p)
        print(v.d1, v.dist)     
        
def DFS(G):
    global time
    for i in G:
        i.c = VertexColor.WHITE  
        i.p = None
    time = 0
    for i in G:
        if i.c == VertexColor.WHITE:
            DFS_Visit(G, i)



def DFS_Visit(G, u):
    global time
    global krajnja_lista
    time = time + 1
    u.dist = time
    u.c = VertexColor.GRAY
    for i in u.list:
        if i.c == VertexColor.WHITE:
            i.p = u
            DFS_Visit(G, i)
           
    u.c = VertexColor.BLACK
    time = time + 1
    u.f = time
    krajnja_lista.append(u)
            

if __name__ == "__main__":
    A = Vertex(d1 = 'A');
    B = Vertex(d1 = 'B');
    C = Vertex(d1 = 'C');
    D = Vertex(d1 = 'D');
    E = Vertex(d1 = 'E');
    F = Vertex(d1 = 'F');
    

    lista_vertexa = list()

    A.list.append(B)
    A.list.append(C)
    B.list.append(D)
    C.list.append(B)
    D.list.append(C)
    E.list.append(D)
    E.list.append(F)
    F.list.append(F)
    
    
    lista_vertexa.append(A)
    lista_vertexa.append(B)
    lista_vertexa.append(C)
    lista_vertexa.append(D)
    lista_vertexa.append(E)
    lista_vertexa.append(F)
    

    BFS(lista_vertexa, B)

    for i in lista_vertexa:
        print(i.d1)
        for j in i.list:
            print("--->",j.d1)

    Print_Path(lista_vertexa, D, F)

    DFS(lista_vertexa)
    
    print("**********")
    h = krajnja_lista[::-1]
    for i in h:
        print("****")
        print(i.d1, "-->>")
        print(i.dist)
        print(i.f)
    

