input_file = 'Data/rosalind_orf.txt'
with open(input_file) as f:
    lines = f.readlines()
lines = [i.strip() for i in lines]
fasta = {}
seq = ''
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


#DNA -> RNA and also consider reverse strand
def transcription(dna):
    rna = ''
    for n in dna:
        if n == 'T':
            rna += 'U'
        else:
            rna += n
    return rna

def get_reverse_strand(dna):
    reverse = ''
    for i in range(len(dna)-1, -1, -1):
        if dna[i] == 'A': reverse += 'T'
        elif dna[i] == 'T': reverse += 'A'
        elif dna[i] == 'G': reverse += 'C'
        elif dna[i] == 'C': reverse += 'G'
    return reverse

def get_ORF(rna):
    orfs = []
    orf = ''
    for n in range(0, len(rna)-2, 1):
        if rna[n:n+3] == 'AUG':
            m = n
            while(RNA_codon[rna[m:m+3]] != 'Stop'):
                orf += RNA_codon[rna[m:m+3]]
                m += 3
                if m > len(rna) - 3:
                    orf = ''
                    break
            if orf:
                orfs.append(orf)
                orf = '' 
    return orfs


for k in fasta.keys():
    
    rna = transcription(fasta[k])
    orfs = get_ORF(rna)
    reverse = get_reverse_strand(fasta[k])
    reverse = transcription(reverse)
    orfs += get_ORF(reverse)

unique_orfs = []
for o in orfs:
    if o not in unique_orfs:
        unique_orfs.append(o)

for i in unique_orfs:
    print(i)

