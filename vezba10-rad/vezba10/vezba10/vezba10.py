import sys
from math import inf


from enum import Enum	


class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, p = None, d1 = None, d2 = None, f = None):
        """
        Vertex constructor 
        @param  parent, auxilary data1, auxilary data2
        """
        self.list = []
        self.p = p
        self.d1 = d1   
        self.dist = d2
        self.f = f

class Edge:

    def __init__(self, source = None, destination = None, weight = None):
        self.source = source
        self.destination = destination
        self.weight = weight


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
	

def InitializeSingleSource(G, s):
    for i in G:
        i.dist = inf
        i.p = None
    s.dist = 0

def Relax(u,v,w):
    if v.dist > u.dist + w:
        v.dist = u.dist + w
        v.p = u

def Dijkstra(G,s):
    InitializeSingleSource(G,s)
    S = list()
    Q = G
    while len(Q) is not 0:
        
        index = ExtractMin(Q)
        u = Q.pop(index)
        S.append(u)
        for i in u.list:
            Relax(i.source, i.destination, i.weight)


def ExtractMin(Q):
    min = 0
    for i in range(len(Q)):
        if Q[i].dist < Q[min].dist:
            min = i
    return min   


if __name__ == "__main__":

    vertex_lista = list()

    A = Vertex(d1 = 'A');
    B = Vertex(d1 = 'B');
    C = Vertex(d1 = 'C');
    D = Vertex(d1 = 'D');
    E = Vertex(d1 = 'E');
    

    AB = Edge(A, B, 10)
    AD = Edge(A, D, 5)
    BC = Edge(B, C, 1)
    BD = Edge(B, D, 2)
    CE = Edge(C, E, 4)
    DB = Edge(D, B, 3)
    DC = Edge(D, C, 9)
    DE = Edge(D, E, 2)
    EA = Edge(E, A, 7)
    EC = Edge(E, C, 6)

    A.list.append(AB)
    A.list.append(AD)
    B.list.append(BC)
    B.list.append(BD)
    C.list.append(CE)
    D.list.append(DB)
    D.list.append(DC)
    D.list.append(DE)
    E.list.append(EA)
    E.list.append(EC)

    vertex_lista.append(A)
    vertex_lista.append(B)
    vertex_lista.append(C)
    vertex_lista.append(D)
    vertex_lista.append(E)

    

    Dijkstra(vertex_lista, A)

    vertex_lista.append(A)
    vertex_lista.append(B)
    vertex_lista.append(C)
    vertex_lista.append(D)
    vertex_lista.append(E)
    for i in vertex_lista:
        print(i.d1 , "--->", i.dist)
        for j in i.list:
            print(j.destination.d1)


