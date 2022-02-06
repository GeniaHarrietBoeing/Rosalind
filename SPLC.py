input_file = 'Data/rosalind_splc.txt'
with open(input_file) as f:
    lines = f.readlines()
lines = [i.strip() for i in lines]
fasta = {}
seq = ''

full_seq_id = lines[0][1:]
for l in lines:
    if l[0] == '>':
        if l != lines[0]:
            fasta[seq_name] = seq
            seq = ''
        seq_name = l[1:]
    else:
        seq += l
fasta[seq_name] = seq

file = 'Data/RNA_Codon_Table.txt'
with open(file) as f:
    lines = f.readlines()
RNA_codon = {}
lines = [i.strip().split() for i in lines]
for l in lines:
    for i in range(0, len(l), 2):
        RNA_codon[l[i]] = l[i+1]

#concatenate only the exons 
for k in fasta.keys():
    if k != full_seq_id:
        for i in range(0, len(fasta[full_seq_id])):
            if fasta[full_seq_id][i:i+len(fasta[k])] == fasta[k]:
                fasta[full_seq_id] = fasta[full_seq_id][:i] + fasta[full_seq_id][i+len(fasta[k]):]
#translate:
dna = ''
for aa in fasta[full_seq_id]:
    if aa == 'T': dna += 'U'
    else: dna += aa
fasta[full_seq_id] = dna

#translate:
protein = ''
for i in range(0, len(fasta[full_seq_id]), 3):
    aa = RNA_codon[fasta[full_seq_id][i:i+3]]
    if aa != 'Stop':
        protein += aa
    else: break
print(protein)
 
 
 
 
 
 
