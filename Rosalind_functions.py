def read_fasta(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    lines = [i.strip() for i in lines]
    fasta = {}
    seq = ''

    full_seq_id = lines[0][1:]
    for l in lines:
        if l[0] == '>':
            if l != lines[0]:
                fasta[seq_name] = seq
                seq = ''
            seq_name = l[1:]
        else:
            seq += l
    fasta[seq_name] = seq
    
    return fasta

def read_RNA_Codon_file(file_name='Data/RNA_Codon_Table.txt'):
    with open(file_name) as f:
        lines = f.readlines()
    RNA_codon = {}
    lines = [i.strip().split() for i in lines]
    for l in lines:
        for i in range(0, len(l), 2):
            RNA_codon[l[i]] = l[i+1]
    return RNA_codon
