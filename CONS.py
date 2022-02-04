import numpy as np

input_file = 'Data/rosalind_cons.txt'

with open(input_file) as f:
    lines = f.readlines()
lines = [i.strip() for i in lines]

fasta = {}
seq = ''
for i in lines:
    if i[0] == '>':
        if i != lines[0]:
            fasta[seq_name] = seq
            seq = ''
        seq_name = i[1:]
    else: seq += i
fasta[seq_name] = seq

Profile = np.zeros((4, len(list(fasta.values())[0])))
nucleotides = 'ACGT'
for k in fasta.keys():
    for n in range(0, len(fasta[k])):
        for i in range(0, len(nucleotides)):
            if nucleotides[i] == fasta[k][n]:
                Profile[i, n] += 1

consensus = ''
for n in range(0, Profile.shape[1]):
    max_n = 0
    max_idx = 0
    for i in range(0, Profile.shape[0]):
        if Profile[i, n] > max_n:
            max_n = Profile[i, n]
            max_idx = i
    consensus += nucleotides[max_idx]

print(consensus)
for i in range(0, len(nucleotides)):
    line = nucleotides[i] + ':'
    for k in Profile[i, :]:
        line += ' ' + str(int(k)) 
    print(line)
