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

def  BinarySearch(A, p, r, key):
    if p >= r:
        return -1
    q = (p + r) // 2 + 1
    if A[q] == key:
        return q
    elif A[q] < key:
        return BinarySearch(A, q + 1, r, key)
    else:
        return BinarySearch(A, p, q, key)

A = []
s = random.randint(5, 10)
for i in range(0, s):
    A.append(random.randint(0, 100))
A = InsertionSort(A, len(A))
key = random.choice(A)

print(A)
print(key)
print(BinarySearch(A, 0, len(A)-1, key))