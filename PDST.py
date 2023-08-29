from Rosalind_functions import read_fasta
import numpy as np

input_file = 'Data/rosalind_pdst.txt'
fasta = read_fasta(input_file)

seqs = list(fasta.values())
n = len(seqs)
dist = np.zeros((n, n))

def dist_seq(seq1, seq2):
    diff = 0
    for i in range(0, len(seq1)):
        if seq1[i] != seq2[i]:
            diff += 1
    return diff/len(seq1)

for i in range(0, len(seqs)):
    for j in range(0, len(seqs)):
        dist[i][j] = dist_seq(seqs[i], seqs[j])

for i in range(0, n):
    print(' '.join([str(i) for i in dist[i]]))
