#python3
import random

def NaiveFibonacci(a):
    if a == 0:
        return 0
    if a == 1:
        return 1
    else:
        return NaiveFibonacci(a - 1) + NaiveFibonacci(a - 2)
    
def LinearFibonacci(a):
    A = [0, 1]
    for i in range(2, a + 1):
        A.append(A[i - 1] + A[i - 2])
    return A[a]

def RecursiveSquaring(n):
    basicMatrix = [[1, 1], [1, 0]]
    if n == 0:
        return basicMatrix
    if n == 1:
        return basicMatrix
    else:
        matrix = RecursiveSquaring(n // 2)
        if n % 2 == 0:
            return matrix * matrix
        if n % 2 == 1:
            return ( matrix * matrix) * basicMatrix
        
def AdvanceFibonacci(n):
    matrix = RecursiveSquaring(n)
    return matrix[0][1]

a = random.randint(5,20)
print("the Fibonacci number of ", a, " is ", NaiveFibonacci(a))
print("the Fibonacci number of ", a, " is ", LinearFibonacci(a))
print("the Fibonacci number of ", a, " is ", AdvanceFibonacci(a))