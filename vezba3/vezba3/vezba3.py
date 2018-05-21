import sys
import math


def MergeSort(A, p, r):
    if p<r:
      
        q = ((p+r)//2)
        MergeSort(A,p,q)
        MergeSort(A,q+1,r)
        Merge(A, p , q , r)

def Merge(A, p, q, r):
        print(A)
        n1 = q - p + 1
        n2 = r - q 
        L = []
        R = []
        for i in range(n1):
            L.append(A[p+i])
        for j in range(n2):
            R.append(A[q+j+1])
        L.append(math.inf)
        R.append(math.inf)
        print("LEVI DEO",L)
        print("DESNI DEO",R)
        i = 0
        j = 0

        for k in range(p,r+1):
            if L[i] <= R[j]:
                A[k] = L[i]
                i = i+1
            else:
                A[k] = R[j]
                j = j+1 



if __name__ == "__main__":
    niz = [3,3,3,3,2,2,2,2,2]
    MergeSort(niz,0,len(niz)-1)

    print(niz)