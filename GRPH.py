input_file = 'Data/rosalind_grph.txt'
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
    else:
        seq += i
fasta[seq_name] = seq

k = 3

for k in fasta.keys():
    suffix = fasta[k][-3:]
    for j in fasta.keys():
        if k != j:
            prefix = fasta[j][0:3]
            if suffix == prefix:
                print(k, j)
            
