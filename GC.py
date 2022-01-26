input_file = 'Data/rosalind_gc.txt'


def read_FASTA(file):
    with open(file) as f:
        data = f.readlines()

    fasta = {}
    seq_name = ''
    seq = ''
    for i in range(0, len(data)):
        if data[i][0] == '>':
            if i != 0:
                fasta[seq_name] = seq
            seq_name = data[i][1:-1]
            seq = ''
        else:
            seq += data[i].strip()
 
    fasta[seq_name] = seq

    return fasta

def get_GC_content(seq):
    tot = len(seq)
    GC_count = 0
    for i in seq:
        if i in 'GC':
            GC_count += 1
    return (GC_count / tot) * 100

fasta = read_FASTA(input_file)
max_GC = 0
max_seq = ''
for i in fasta.keys():
    
    GC = get_GC_content(fasta[i])
    if GC > max_GC:
        max_seq = i
        max_GC = GC

print(max_seq + '\n' + str(max_GC))
