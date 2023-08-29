input_file = 'Data/rosalind_lexf.txt'
with open(input_file) as f:
    lines = f.readlines()

symbols = lines[0].strip().split()
n = int(lines[1])

def add_all_symbols(word, n, symbols):
    n -= 1
    if n == 0:
        print(word)
    else:
        for i in symbols:
            add_all_symbols(word+i, n, symbols)

for i in symbols:
    add_all_symbols(i, n, symbols)
