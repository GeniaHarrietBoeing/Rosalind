input_file = 'Data/rosalind_ba1f.txt'
with open(input_file) as f:
    line = f.read()
seq = line.strip()

skew = [0]*(len(seq)+1)
for n in range(0, len(seq)):
    if seq[n] == 'C':
        skew[n+1] = skew[n] - 1
    elif seq[n] == 'G':
        skew[n+1] = skew[n] + 1
    else:
        skew[n+1] = skew[n]

min_skew = 0
for i in range(0, len(skew)):
    if skew[i] < min_skew: min_skew = skew[i]
result = []
for i in range(0, len(skew)):
    if skew[i] == min_skew:
        result += [str(i)]
print(' '.join(result))
