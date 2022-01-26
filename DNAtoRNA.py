ex_input = 'GATGGAACTTGACTACGTAAATT'

input_file = 'Data/rosalind_rna.txt'
with open(input_file) as f:
    data = f.readline()
data = data.strip()

def DNAtoRNA(data):
    data = list(data)
    for i in range(0, len(data)):
        if data[i] == 'T':
            data[i] = 'U'
    rna_data = ''
    return rna_data.join(data)

print(DNAtoRNA(ex_input))

print(DNAtoRNA(data))
