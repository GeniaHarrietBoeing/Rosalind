file = 'Data/RNA_Codon_Table.txt'
Codon_RNA = {}
with open(file) as f:
    data = f.readlines()

data = [i.strip().split() for i in data]
for i in data:
    for j in range(0, len(i), 2):
        Codon_RNA[i[j]] = i[j+1]


input_file = 'Data/rosalind_prot.txt'
with open(input_file) as f: 
    RNA = f.read().strip()

AA_str = ''
for i in range(0, len(RNA), 3):
    if Codon_RNA[RNA[i:i+3]] == 'Stop':
        break
    AA_str += Codon_RNA[RNA[i:i+3]]

print(AA_str)
