import math
import random

def generate_random_graph():
    number_of_vertexes = random.randint(3, 6)
    vertexi = []
    for i in range(1, number_of_vertexes+1):
        vertexi.append(Vertex(data=i))
    for vertex in vertexi:
        number_of_edges = random.randint(0, 3)
        vertex.edges = []
        for i in range(0, number_of_edges):
            vertex.edges.append(Edge(source=vertex, dest=vertexi[random.randint(0, number_of_vertexes-1)], weight=random.randint(0, 15)))

    return vertexi

class Vertex:
    def __init__(self, data = None, data2 = None, edges = None, par = None):
        self.data = data
        self.data2 = data2
        self.edges = edges
        self.parent = par

class Edge:
    def __init__(self, source = None, dest = None, weight = None):
        self.source = source
        self.dest = dest
        self.weight = weight

def initialize_single_source(G, s):
    for vertex in G:
        vertex.data2 = math.inf
        vertex.parent = Vertex(data = 'Nothing')
    s.data2 = 0

def relax(u, v, w):
    if v.data2 > (u.data2 + w(u, v)):
        v.data2 = u.data2 + w(u, v)
        v.parent = u

def w(u, v):
    for i in u.edges:
        if i.dest == v:
            temp = i
    return temp.weight

def extract_min(Q):
    min = Q[0]
    for i in Q:
        if min.data2 > i.data2:
            min = i

    Q.remove(min)
    return min

def dijkstra(G, w, s):
    initialize_single_source(G, s)
    S = []
    Q = G[:]
    while len(Q)> 0:
        u = extract_min(Q)
        S.append(u)
        for edge in u.edges:
            relax(edge.source, edge.dest, w)

s = Vertex(data = 's')
y = Vertex(data='y')
t = Vertex(data='t')
x = Vertex(data='x')
z = Vertex(data='z')

s.edges = [Edge(source = s, dest = t, weight=10), Edge(source = s, dest = y, weight=5)]
t.edges = [Edge(source = t, dest = y, weight=2), Edge(source = t, dest = x, weight=1)]
x.edges = [Edge(source = x, dest = z, weight=4)]
z.edges = [Edge(source = z, dest = x, weight=6), Edge(source = z, dest = s, weight=7)]
y.edges = [Edge(source = y, dest = t, weight=3), Edge(source = y, dest = x, weight=9), Edge(source = y, dest = z, weight=2)]

vertexes = [s, y, t, x, z]

'''for i in vertexes:
    for j in i.edges:
        print(j.source.data, j.dest.data, j.weight) '''

dijkstra(vertexes, w, s)

#for vertex in vertexes:
 #   print(vertex.parent.data, vertex.data2)


randgraph = generate_random_graph()


for i in randgraph:
        print(i.data , "--->")
        for j in i.edges:
            print(j.dest.data)


dijkstra(randgraph, w, randgraph[0] )

for i in randgraph:
        print(i.data , "--->" ,i.data2)
        for j in i.edges:
            print(j.dest.data)

#for i in randgraph:
  #  print(i.parent.data, i.data2)