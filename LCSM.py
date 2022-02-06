import Rosalind_functions as Rf

input_file = 'Data/rosalind_lcsm.txt'
fasta = Rf.read_fasta(input_file)

motifs = []
def search_motif(motif=''):
    global motifs
    new_motifs = []

    for n in 'ACTG':
        new_motif = motif + n
        in_all_seq = True
        for v in fasta.values():
            if new_motif not in v:
                in_all_seq = False
        if in_all_seq:
            new_motifs.append(new_motif) 

    if new_motifs:
        motifs += new_motifs
        for m in new_motifs:
            search_motif(m)

search_motif()
max_len = 0
max_idx = 0
for i in range(0, len(motifs)):
    if len(motifs[i]) > max_len:
        max_len = len(motifs[i])
        max_idx = i
print(motifs[max_idx])
