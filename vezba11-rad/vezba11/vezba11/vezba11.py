import sys
from math import inf

lista1 = list()

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

def makeGraph():
    graph = list()

    a = Vertex(d1 = 'a');
    b = Vertex(d1 = 'b');
    c = Vertex(d1 = 'c');
    d = Vertex(d1 = 'd');
    e = Vertex(d1 = 'e');
    f = Vertex(d1 = 'f');
    g = Vertex(d1 = 'g');
    h = Vertex(d1 = 'h');

    ab = Edge(a, b, 8)
    ac = Edge(a, c, 6)
    bd = Edge(b, d, 10)
    cd = Edge(c, d, 15)
    ce = Edge(c, e, 9)
    de = Edge(d, e, 14)
    df = Edge(d, f, 4)
    ef = Edge(e, f, 13)
    eg = Edge(e, g, 17)
    fg = Edge(f,g, 7)

    a.list.append(ab)
    a.list.append(ac)
    b.list.append(bd)
    c.list.append(cd)
    c.list.append(ce)
    d.list.append(de)
    d.list.append(df)
    e.list.append(ef)
    e.list.append(eg)
    f.list.append(fg)

    graph.append(a)
    graph.append(b)
    graph.append(c)
    graph.append(d)
    graph.append(e)
    graph.append(f)
    graph.append(g)

    return graph

def GetInDegrees(graph):
    inList = list()
    num = 0

    for i in graph:
        for j in graph:
            for k in j.list:
                if i == k.destination:
                    num = num + 1
        inList.append(num)
        num = 0
    return inList



def GetOutDegrees(graph):
    outList = list()

    for i in graph:
        outList.append(len(i.list))

    return outList
    

def InitializeSingleSource(G, s):
    for i in G:
        i.dist = inf
        i.p = None
    s.dist = 0

def Relax(u,v,w):
    if v.dist > u.dist + w:
        v.dist = u.dist + w
        v.p = u


def BellmanFord(G, s):
    InitializeSingleSource(G,s)
    for i in G:
        for j in i.list:
            Relax(j.source, j.destination, j.weight) 
    for i in G:
        for j in i.list:
            if j.source.dist > j.destination.dist + j.weight:
                return False
    return True 

def Print_Path(G,s,v):
    
    global lista1
    
    if v == s:
        print(s.d1)
    elif v.p == None:
        print("No path from " ,s.d1, " to ",v.d1, " exist")
    else:
        Print_Path(G,s,v.p)
        lista1.append(v)

    return lista1

def ShortestPath(graph, A, B):
    global lista1
    lista1 = list()
    BellmanFord(graph, A)
    lista1 = Print_Path(graph, A,B)
    for i in lista1:
        print("-->" + i.d1)
    print(B.dist)


    
def UpdateEdge(graph, A, B, weight):
    k = 0
    for i in A.list:
        if i.destination == B:
            i.weight = weight
            k = 1
    if k == 0:
        A.list.append(Edge(A,B,weight))

if __name__  == "__main__":

    graph = list()
    
    graph =  makeGraph()
    outList = GetOutDegrees(graph)
    inList = GetInDegrees(graph)

    BellmanFord(graph, graph[0])
    UpdateEdge(graph, graph[4], graph[6], 0)
    BellmanFord(graph, graph[0])

    ShortestPath(graph, graph[0], graph[6])

    for i in graph:
        print(i.d1 , "--->", i.dist)
        #for j in i.list:
            #print(j.destination.d1)

