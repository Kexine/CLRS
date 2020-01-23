#python3
import random
def InsertionSort(A,n):
    for j in range(1,n):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
    return A

A = []
s = random.randint(5,10)
for i in range(1,s):
    A.append(random.randint(0,100))
print(A)
print(InsertionSort(A,len(A)))