file = 'Data/RNA_Codon_Table.txt'
RNA_Codon = {}
with open(file) as f:
 data = f.readlines()

data = [i.strip().split() for i in data]

for i in data:
    for j in range(1, len(i), 2):
        if i[j] not in RNA_Codon.keys():    
            RNA_Codon[i[j]] = 1
        else:
            RNA_Codon[i[j]] += 1

input_file = 'Data/rosalind_mrna.txt'
with open(input_file) as f:
    protein = f.read()
protein = protein.strip()

n = 10**6
number_rna = 1
for aa in protein:
    if number_rna >= n:
        number_rna = number_rna % n
    number_rna *= RNA_Codon[aa]

if number_rna >= n:
    number_rna = number_rna % n
number_rna *= RNA_Codon['Stop']

if number_rna >= n:
    number_rna = number_rna % n
print('number of different rnas:    ', number_rna)
