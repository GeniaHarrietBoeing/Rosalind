input_file = 'Data/rosalind_ba1e.txt'
with open(input_file) as f:
    lines = f.readlines()
seq = lines[0].strip()
lines = lines[1].strip().split()
lines = [int(i) for i in lines]
k = lines[0]
L = lines[1]
t = lines[2]

clumps = []

for l in range(0, len(seq) - L):
    sub_seq = seq[l:l+L]
    for i in range(0, len(sub_seq) - k):
        kmer = sub_seq[i:i+k]
        counter = 0
        if kmer not in clumps:
            for s in range(0, len(sub_seq) - k):
                if kmer == sub_seq[s:s+k]:
                    counter += 1
            if counter >= t:
                clumps.append(kmer)

print(' '.join(clumps)) 
    
