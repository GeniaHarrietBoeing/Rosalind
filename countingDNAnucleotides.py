ex_data = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
input_file = 'Data/rosalind_dna.txt'
with open(input_file) as f:
    data = f.readlines()
data = data[0].strip()


A = 0
G = 0
T = 0
C = 0


for i in data:
    if i == 'A':
        A += 1
    elif i == 'G':
        G += 1
    elif i == 'T':
        T += 1
    elif i == 'C':
        C += 1

print(A ,' ' , C, ' ', G, ' ', T)
