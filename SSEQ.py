import Rosalind_functions as Rf

input_file = 'Data/rosalind_sseq.txt'
fasta = Rf.read_fasta(input_file)
seq = ''
motif = ''
for k in fasta.keys():
    if motif == '':
        motif = fasta[k]
    if len(fasta[k]) < len(motif):
        motif = fasta[k]
        for s in fasta.keys():
            if k != s: seq = fasta[s]

result = []
for s in range(0, len(seq)):
    if seq[s] == motif[0]:
        result += [str(s + 1)]
        if len(motif) > 1:
            motif = motif[1:]
        else:
            break   
print(' '.join(result))
