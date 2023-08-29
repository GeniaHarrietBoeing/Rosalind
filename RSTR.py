input_file = 'Data/rosalind_rstr.txt'
with open(input_file) as f:
    lines = f.readlines()

seq = lines[1].strip()
n = int(lines[0].split()[0])
GC_content = float(lines[0].split()[1])

nr_GC = 0
nr_AT = 0
for i in seq:
    if i in 'GC':
        nr_GC += 1
    else:
        nr_AT += 1

#probabilty getting the same sequence with gc content GC_prob

prob_same = (GC_content/2)**nr_GC * ((1-GC_content)/2)**nr_AT

#probability of at least one sequence among n being equal to seq 

prob_equal = 1 - (1 - prob_same)**n
print(prob_equal)

