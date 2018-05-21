import sys

A = [9,5,16,1,27,34,8,2,17]
heapSize=len(A)

def Parent(i):
    return i/2
    
def Left(i):
    return 2*i+1

def Right(i):
    return 2*i+2

def MaxHeapify(A,heapSize,i):
    largest = i
    l=Left(i)
    r=Right(i)
    
    if l<heapSize and A[l]>A[largest]:
        largest = l
       
    else:
         largest = i
    if r<heapSize and A[r]>A[largest]:
        largest = r
        
    if largest is not i :
       
        A[i],A[largest] = A[largest],A[i]
        MaxHeapify(A,heapSize,largest)

def BuildMaxHeap(A):
    heapSize=len(A)
    
    for i in range(heapSize,-1,-1):
        
        MaxHeapify(A,heapSize,i)


def Heapsort(A):

    BuildMaxHeap(A)
    for i in range(len(A)-1,0,-1):
        
        A[i],A[0]=A[0],A[i]
#        heapSize=heapSize-1
        MaxHeapify(A,i,0)


    
def bucketSort(A):  
    n=len(A)-1
    buckets=[]
    for j in range(n-1):
        buckets.append([])
    for i in range(n-1):
        buckets[int(10*A[i])].append(A[i])
    
    for i in range(n-1):
        Heapsort(buckets[i])

    for j in range(n-1):
        for k in range(buckets[j]):
 
            A[j] = buckets[k].pop      
    


if __name__ == "__main__":
    
    Heapsort(A)
    print(A)


    for i in range((len(A))-1):
        A[i] = A[i]/100

    bucketSort(A)

    for i in range((len(A))-1):
        A[i] = A[i]*100