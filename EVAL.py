input_file = 'Data/rosalind_eval.txt'
with open(input_file) as f:
    lines = f.readlines()

seq = lines[1].strip()
n = int(lines[0])
A = [float(i) for i in lines[2].split()]


nr_GC = 0
nr_AT = 0
for i in seq:
    if i in 'GC':
        nr_GC += 1
    else:
        nr_AT += 1

results = []
for i in A:
    #probabilty getting the same sequence with gc content GC_prob

    prob_same = (i/2)**nr_GC * ((1-i)/2)**nr_AT

    expected_occurences = (n - len(seq) + 1)*prob_same
    results.append(str(expected_occurences))

print(' '.join(results))
