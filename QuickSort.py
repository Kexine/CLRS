#python3
import random
A = []

def Partition(A, p, q):
    it = random.randint(p, q)
    A[p], A[it] = A[it], A[p]
    x = A[p]
    i = p
    for j in range (p + 1, q):
        if A[j] <= x:
            i +=1
            A[i], A[j] = A[j], A[i]
    A[p], A[i] = A[i], A[p]
    return i
    
def QuickSort(A, p, q):
    if p < q:
        r = Partition(A, p, q)
        QuickSort(A, p, r - 1)
        QuickSort(A, r + 1, q)
    return A

print("Now displaying QuickSort")
s = random.randint(5, 20)
for i in range(0, s):
    A.append(random.randint(0,100))
print(A)
print(QuickSort(A, 0, len(A)-1))