input_file = 'Data/rosalind_ba1g.txt'
with open(input_file) as f:
    lines = f.readlines()
lines = [i.strip() for i in lines]


hamming_distance = 0
for n in range(0, len(lines[0])):
    if lines[0][n] != lines[1][n]:
        hamming_distance += 1

print(hamming_distance)
