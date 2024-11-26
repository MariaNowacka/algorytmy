#zadanie 1
import random 
n=3
#1.1
def wielomian(n):
    a=[]
    for i in range(0,n+1):
        a.append(random.randint(-20, 20))
    return a
a=wielomian(n)
print(a)
def oblx(x):
    p=0
    for i in range(0,n+1):
        p+=a[i]*x**i
    return p

print(oblx(1))
#1.2
def oblx2(x):
    tab=[]
    p=0
    tab.append(1/x)
    for i in range(0,n+1):
        z=x*float(tab[i])
        p+=a[i]*z
        tab.append(z)
    return p

print(oblx2(1))

#1.3
#O(2n)

#zadanie 2
def example1(S):
    """Return the sum of the elements in sequence S."""
    n = len(S)
    total = 0
    for j in range(n):
    total += S[j]
    return total
def example2(S):
    """Return the sum of the elements with even index in sequence S."""
    n = len(S)
    total = 0
    for j in range(0, n, 2):
        total += S[j]
    return total
def example3(S):
    """Return the sum of the prex sums of sequence S."""
    n = len(S)
    total = 0
    for j in range(n):
        for k in range(1+j):
            total += S[k]
    return total
def example4(A, B): # assume that A and B have equal length
    """Return the number of elements in B equal to the sum of prex
    sums in A."""
    n = len(A)
    count = 0
    for i in range(n):
        total = 0
        for j in range(n):
            for k in range(1+j):
                total += A[k]
        if B[i] == total:
            count += 1
    return count
