import numpy as np

input_file = 'Data/rosalind_prob.txt'
with open(input_file) as f:
    lines = f.readlines()
lines = [i.strip() for i in lines]
seq = lines[0]
A = [float(i) for i in lines[1].split()]

nr_GC = 0
nr_AT = 0
for n in seq:
    if n in 'GC': nr_GC += 1
    if n in 'AT': nr_AT += 1

result = []
for gc_content in A:
    prob = np.log10((1-gc_content)/2) * nr_AT + np.log10(gc_content/2) * nr_GC
    result.append(str(prob))

print(' '.join(result))
