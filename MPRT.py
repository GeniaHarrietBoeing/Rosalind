import sys

input_file = str(sys.argv[1])
data_folder = str(sys.argv[2])


with open(input_file) as f:
    lines = f.readlines()
Uniprot_ID = [i.strip() for i in lines]

Uniprot_motifs = {}
for uid in Uniprot_ID:
    motif_start = []
    with open(data_folder + '/' + uid + '.fasta') as f:
        fasta = f.readlines()
    fasta = [f.strip() for f in fasta]
    fasta = fasta[1:]
    seq = ''.join(fasta)

    for i in range(0, len(seq)-3):
        if (seq[i] == 'N' and
            seq[i+1] != 'P' and
            seq[i+2] in 'ST' and 
            seq[i+3] != 'P'):
            motif_start.append(str(i+1))
    
    Uniprot_motifs[uid] = motif_start

for k in Uniprot_motifs.keys():
    if Uniprot_motifs[k]:
        print(k)
        print(' '.join(Uniprot_motifs[k]))
