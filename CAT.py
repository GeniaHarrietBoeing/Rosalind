from Rosalind_functions import read_fasta


input_file = 'Data/rosalind_cat.txt'
fasta = read_fasta(input_file)

seq = list(fasta.values())[0]

def count_catalan(n):
    if n == 0 or n == 1:
        return 1
    else:
        c_n = 0
        for k in range(1, n+1):
            c_n += count_catalan(k-1) * count_catalan(n-k)

    return c_n

def even_AU_GC(seq):
    n_A = 0
    n_U = 0
    n_G = 0
    n_C = 0
    for i in seq:
        if i == 'A': n_A += 1
        elif i == 'U': n_U += 1 
        elif i == 'G': n_G += 1
        elif i == 'C': n_C += 1
    if n_A == n_U and n_G == n_C:
        return True
    else:
        return False

def count_rna_catalan(n, seq, memoization):
    if seq in memoization.keys():
        return memoization[seq], memoization

    #need to keep n_A == n_U and likewise for G,C
    if len(seq) == 2 or len(seq) == 0:
        c_n = 1
        return c_n, memoization
    else:
        c_n = 0
        for k in range(1, n+1):

            connected = seq[0]+seq[2*k-1]
            if 2*k-1 > 1:
                in_between = seq[1:2*k-1]
            else:
                in_between = ''
            following = seq[2*k:]

            if even_AU_GC(in_between) and even_AU_GC(following):
                c_k_min_1, memoization = count_rna_catalan(k-1, in_between, memoization)
                c_n_min_k, memoization = count_rna_catalan(n-k, following, memoization)
                if in_between not in memoization.keys():
                    memoization[in_between] = c_k_min_1
                if following not in memoization.keys():
                    memoization[following] = c_n_min_k
                c_n += c_k_min_1 * c_n_min_k
    return c_n, memoization
memoization = {}
nr_noncrossings, memoization = count_rna_catalan(len(seq)//2, seq, memoization)
print(nr_noncrossings % 10**6)
