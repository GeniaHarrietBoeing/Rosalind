input_file = 'Data/rosalind_lexv.txt'
with open(input_file) as f:
    lines = f.readlines()
lex = lines[0].strip().split()
n = int(lines[1])
def add_letter(string, lex, n):
    if len(string) < n:
        for i in lex:
            new_string = string + i
            print(new_string)
            add_letter(new_string, lex, n)

add_letter('', lex, n)
