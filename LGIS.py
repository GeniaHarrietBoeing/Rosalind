input_file = 'Data/rosalind_lgis.txt'
with open(input_file) as f:
    lines = f.readlines()

n = int(lines[0].strip())
permutation = lines[1].strip().split()
permutation = [int(i) for i in permutation]
#n = 5
#permutation = [5, 1, 4, 2, 3]


# This is from luyang93
seq = permutation 

# m keeps track of the number of following entries in the sequence that are larger
# the condition m[i] <= m[j] makes sure that a lower number doesn't get a higher m from larger following entries
# which have a smaller number of following increasing numbers
m = [0] * n
for i in range(n-2, -1, -1):
    for j in range(n-1, i, -1):
        if seq[i] < seq[j] and m[i] <= m[j]:
            m[i] += 1

max_m = max(m)
incr_subseq = []
for i in range(0, len(m)):
    if m[i] == max_m:
        incr_subseq.append(seq[i])
        max_m -= 1

m = [0] * n
for i in range(n-2, -1, -1):
    for j in range(n-1, i, -1):
        if seq[i] > seq[j] and m[i] <= m[j]:
            m[i] += 1

max_m = max(m)
decr_subseq = []
for i in range(0, len(m)):
    if m[i] == max_m:
        decr_subseq.append(seq[i])
        max_m -= 1



print(' '.join([str(i) for i in incr_subseq]))
print(' '.join([str(i) for i in decr_subseq]))        


