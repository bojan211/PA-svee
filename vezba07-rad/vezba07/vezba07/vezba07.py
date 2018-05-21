import math
import random
import time

class Data:
    def __init__(self, k=None, l=None):
        self.key = k
        self.literal = l
    def getKey(self):
            return self.key
    def getLiteral(self):
            return self.literal



m = 100
p = 10007
a = random.randint(1, p)
b = random.randint(0, p)

input = []
for i in range(0, 10000):
    temp = Data(i, random.randint(1, 100000))
    input.append(temp)

def division_method(key):
    global m
    return key%m

def multiplication_method(key):
    global m
    return math.floor(m*((key*0.618033)%1))

def universal_hashing(key):
    global m, a, b, p
    return ((a*key+b)%p)%m

def chained_hash_insert(T, x):
    ind = division_method(x.getKey())
    if chained_hash_search(T, x.getKey()) == None:
        T[ind].append(x)
    else:
        chained_hash_delete(T, x)
        T[ind].append(x)


def chained_hash_search(T, k):
    ind = division_method(k)
    for item in T[ind]:
        if item.getKey() == k:
            return item
    return None

def chained_hash_delete(T, x):
    ind = division_method(x.getKey())
    T[ind].remove(x)


if __name__ == "__main__":
    A =[]
    for i in range(0, m):
        A.append([])

    B =[]
    for i in range(0, m):
        B.append([])

    C =[]
    for i in range(0, m):
        C.append([])

    start_time = time.clock()

    for i in range(0, 10000):
        chained_hash_insert(A, input[i]) 

    end_time1 = time.clock() - start_time
    print("Duration: ", end_time1)

    

    
        
           




