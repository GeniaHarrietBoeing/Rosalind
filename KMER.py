from Rosalind_functions import read_fasta

input_file = 'Data/rosalind_kmer.txt'
fasta = read_fasta(input_file)
seq = list(fasta.values())[0]
kmers = []

def add_letter(string, kmers):
    if len(string) == 4:
        kmers.append(string)
    else:
        for i in ['A', 'C', 'G', 'T']:
            new_string = string + i
            kmers = add_letter(new_string, kmers)
    return kmers

kmers = add_letter('', kmers)

counts = []
for k in kmers:
    occurences = 0
    for i in range(0, len(seq)-3):
        if seq[i:i+4] == k:
            occurences += 1
    counts.append(str(occurences))

print(' '.join(counts))
