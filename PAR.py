input_file = 'Data/rosalind_par.txt'
with open(input_file) as f:
    lines = f.readlines()
a = [int(i) for i in lines[1].strip().split()]

smaller = []
larger = []
for i in range(1, len(a)):
    if a[i] > a[0]:
        larger.append(a[i])
    elif a[i] < a[0]:
        smaller.append(a[i])

result = smaller + [a[0]] + larger
print(' '.join([str(i) for i in result]))
