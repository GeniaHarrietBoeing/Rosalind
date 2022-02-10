input_file = 'Data/rosalind_ba1d.txt'
with open(input_file) as f:
    lines = f.readlines()
lines = [i.strip() for i in lines]
sub = lines[0]
seq = lines[1]
result = []
for i in range(0, len(seq) - len(sub) + 1):
    if seq[i:i+len(sub)] == sub:
        result += [str(i)]

print(' '.join(result))
