#python3
import random

def MergeSort(A, p, r):
    q = (p + r) // 2
    if p < r:
        MergeSort(A, p, q)
        MergeSort(A, q + 1, r)
    return Merge(A, p, q, r)

MAX = 10000

def Merge(A, p, q, r):
    L = []
    R = []
    for i in range(p, q + 1):
        L.append(A[i])
    for i in range(q + 1, r + 1):
        R.append(A[i])
    L.append(MAX)
    R.append(MAX)
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] < R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
    return A

A = []
s = random.randint(5, 10)
for i in range(0, s):
    A.append(random.randint(0, 50))
print(A)
print(MergeSort(A, 0, len(A)-1))