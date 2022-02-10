import Rosalind_functions as Rf

input_file = 'Data/rosalind_long.txt'
fasta = Rf.read_fasta(input_file)

#construct all superstrings and choose shortest one
def construct_superseq(seq, included_seq, fasta, new_seq):
    for k in fasta.keys():
        if k not in included_seq:
           for i in range(len(fasta[k])//2-1, len(fasta[k])):
                if seq[0:i] == fasta[k][-i:]:
                    new_seq[fasta[k] + seq[i:]] = included_seq + [k]
                if seq[-i:] == fasta[k][0:i]:
                    new_seq[seq + fasta[k][i:]] = included_seq + [k]
    return new_seq

included_seq = [list(fasta.keys())[0]]
seqs = {fasta[list(fasta.keys())[0]]: included_seq}
superseqs = []
while(len(seqs) > 0):
    new_seqs = {}
    for s in seqs.keys():
        new_seqs = construct_superseq(s, seqs[s], fasta, new_seqs)
    to_pop = []
    for k in new_seqs.keys():
        if len(new_seqs[k]) == len(fasta.keys()):
            superseqs.append(k)
            to_pop.append(k)
    for i in to_pop:
        new_seqs.pop(i)
    seqs = new_seqs

min_length = len(superseqs[0])
min_seq = superseqs[0]
for s in superseqs:
    if len(s) < min_length:
        min_seq = s
        min_length = len(s)

print(min_seq)
print(len(superseqs))
