input_file = 'Data/rosalind_sset.txt'
with open(input_file) as f:
    lines = f.readlines()
n = int(lines[0])
print(n)
print(2**n%10**6)
