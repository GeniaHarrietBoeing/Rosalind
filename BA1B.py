input_file = 'Data/rosalind_ba1b.txt'
with open(input_file) as f:
    lines = f.readlines()
lines = [i.strip() for i in lines]
seq = lines[0]
k = int(lines[1])

kmers = {}
max_count = 1
for i in range(0, len(seq)-(k-1)):
    if seq[i:i+k] in kmers.keys():
        kmers[seq[i:i+k]] += 1
        max_count = max(max_count, kmers[seq[i:i+k]])
    else:
        kmers[seq[i:i+k]] = 1

result = []
for k in kmers.keys():
    if kmers[k] == max_count:
        result.append(k)

print(' '.join(result))
