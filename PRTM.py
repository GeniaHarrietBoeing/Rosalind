input_file = 'Data/rosalind_prtm.txt'
with open(input_file) as f:
    protein = f.read()
protein = protein.strip()

file = 'Data/monoisotopicMassTable.txt'
with open(file) as f:
    lines = f.readlines()
lines = [i.strip().split() for i in lines]

aa_mass = {}
for i in lines:
    aa_mass[i[0]] = float(i[1])

protein_weight = 0
for aa in protein:
    protein_weight += aa_mass[aa]

print('mass of the protein: ', protein_weight)
