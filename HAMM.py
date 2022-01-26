input_file = 'Data/rosalind_hamm.txt'
with open(input_file) as f:
    data = f.readlines()
seq1 = data[0].strip()
seq2 = data[1].strip()

def get_Hamming_dist(seq1, seq2):
    dist = 0
    for i in range(0, len(seq1)):
        if seq1[i] != seq2[i]:
            dist += 1
    return dist

print(get_Hamming_dist(seq1, seq2))

