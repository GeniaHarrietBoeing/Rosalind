input_file = 'Data/rosalind_pper.txt'
with open(input_file) as f:
    lines = f.readlines()
lines = [i.strip().split() for i in lines]
n = int(lines[0][0])
k = int(lines[0][1])
modulo = 10**6

result = 1
for i in range(n, n-k, -1):
    result *= i
    while(result >= modulo):
        result -= modulo

print(result)
