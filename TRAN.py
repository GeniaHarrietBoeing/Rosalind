from Rosalind_functions import read_fasta   

input_file = 'Data/rosalind_tran.txt'
fasta = read_fasta(input_file)

transitions = ['GA', 'CT', 'AG', 'TC']
seqs = list(fasta.values())


n_transitions = 0
n_transversions = 0
for i in range(0, len(seqs[0])):
    if seqs[0][i] != seqs[1][i]:
        if seqs[0][i]+seqs[1][i] in transitions:
            n_transitions += 1
        else:
            n_transversions += 1

print(n_transitions/n_transversions)
