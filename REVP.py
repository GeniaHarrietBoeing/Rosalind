import Rosalind_functions as Rf

input_file = 'Data/rosalind_revp.txt'
fasta = Rf.read_fasta(input_file)

min_len = 4
max_len = 12
DNA_complement = {'A' : 'T', 'T': 'A', 'G': 'C', 'C': 'G'}


def reverse_str(string):
    reverse = ''
    for i in range(len(string)-1, -1, -1):
        reverse += string[i]
    return reverse

def find_reverse_palindrome(seq, length):
    complement = ''
    for n in seq:
        complement += DNA_complement[n]
    for n in range(0, len(seq)-(length-1)):
        reverse = reverse_str(complement[n:n+length])
        if reverse == seq[n:n+length]:
            print(n+1, length)


for length in range(min_len, max_len+1):
    for k in fasta.keys(): 
        find_reverse_palindrome(fasta[k], length)
