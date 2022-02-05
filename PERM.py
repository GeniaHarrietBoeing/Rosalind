input_file = 'Data/rosalind_perm.txt'
with open(input_file) as f:
    line = f.read()
n = int(line.strip())

nr_permutations = 1
for i in range(1, n+1):
    nr_permutations *= i
print(nr_permutations)

def perm(ele):
    if not ele:
        return []
    
    if len(ele) == 1:
        return [ele]

    l = []
    
    for i in range(0, len(ele)):
        m = ele[i]
        remList = ele[:i] + ele[i+1:]
        for p in perm(remList):
            l.append([m] + p)
    return l

permutations = perm(list(range(1, n+1)))
for i in permutations:
    print(' '.join([str(k) for k in i]))
