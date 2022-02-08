import Rosalind_functions as Rf

input_file = 'Data/rosalind_pmch.txt'
fasta = Rf.read_fasta(input_file)

DNA_complement = {'A' : 'U', 'U': 'A', 'G': 'C', 'C': 'G'}

#total possible number of perfect matchings
#perfect matchings: n edges 
# nr G == nr C and nr U == nr A


for k in fasta.keys():
    nrGC = 0
    nrAU = 0
    for n in fasta[k]:
        if n == 'G': nrGC += 1
        if n == 'A': nrAU += 1

perfect_matchings = 1
for i in range(nrGC, 0, -1):
    perfect_matchings *= i
for i in range(nrAU, 0, -1):
    perfect_matchings *= i

print(perfect_matchings)

