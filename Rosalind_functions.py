def read_fasta(file_name):
    with open(input_file) as f:
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
