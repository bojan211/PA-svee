import sys
import random

def Partition(A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] <= x:
            i = i+1
            A[i],A[j] = A[j],A[i]

    
    A[i+1],A[r] = A[r],A[i+1]

    return i+1

def RandomizedPartition(A, p, r):
    i = random.randint(p,r)
    
    A[r],A[i] = A[i],A[r]
    return Partition(A, p, r)
    
def RandomizedQuicksort(A,p,r):
    if p<r:
        q = RandomizedPartition(A,p,r)
        RandomizedQuicksort(A,p,q-1)
        RandomizedQuicksort(A,q+1,r)


if __name__ == "__main__":
    
    lista = [2,5,3,6,2,242,5,7,8,4,3]

    RandomizedQuicksort(lista,0,len(lista)-1)

    print(lista)