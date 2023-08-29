import re
input_file = 'Data/rosalind_seto.txt'
with open(input_file) as f:
    lines = f.readlines()
n = int(lines[0])
A = [int(re.sub("[^0-9]", "", i)) for i in lines[1].split()]
B = [int(re.sub("[^0-9]", "", i)) for i in lines[2].split()]

def union(A, B, n):
    C = []
    for i in range(1, n+1):
        if i in A or i in B:
            C.append(i)
    return C

def intersection(A, B, n):
    C = []
    for i in range(1, n+1):
        if i in A and i in B:
            C.append(i)
    return C

def subtraction(A, B):
    C = []
    for i in A:
        if i not in B:
            C.append(i)
    return C


U = [i for i in range(1, n+1)]
print('{'+', '.join([str(i) for i in union(A, B, n)])+'}')
print('{'+', '.join([str(i) for i in intersection(A, B, n)])+'}')
print('{'+', '.join([str(i) for i in subtraction(A, B)])+'}')
print('{'+', '.join([str(i) for i in subtraction(B, A)])+'}')
print('{'+', '.join([str(i) for i in subtraction(U, A)])+'}')
print('{'+', '.join([str(i) for i in subtraction(U, B)])+'}')

