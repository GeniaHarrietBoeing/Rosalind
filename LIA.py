import math

input_file = 'Data/rosalind_lia.txt'
with open(input_file) as f:
    data = f.read()
data = data.split()

k = int(data[0])
N = int(data[1])

total = 2**k

prob = 0
for i in range(N, total+1):
    prob  += (math.factorial(total) / (math.factorial(i) * math.factorial(total - i))) * 0.25**i * 0.75**(total - i)


print('prob of at least N AaBb genotypes:   ', prob)
