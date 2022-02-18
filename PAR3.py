input_file = 'Data/rosalind_par3.txt'
with open(input_file) as f:
    lines = f.readlines()
a = [int(i) for i in lines[1].strip().split()]

smaller = []
same = 1
larger = []
for i in range(1, len(a)):
    if a[i] < a[0]:
        smaller.append(a[i])
    elif a[i] == a[0]:
        same += 1
    elif a[i] > a[0]:
        larger.append(a[i])

result = smaller + [a[0]] * same + larger
print(' '.join([str(i) for i in result]))
