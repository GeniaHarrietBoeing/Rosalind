import math

input_file = 'Data/rosalind_aspc.txt'

with open(input_file) as f:
    lines = f.readlines()
lines = lines[0].split()
n = int(lines[0])
m = int(lines[1])

def C(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n-k))


result = 0
for k in range(m, n+1):
    result += C(n, k)

print(int(result) % 10**6)
