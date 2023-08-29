input_file = 'Data/rosalind_mer.txt'

with open(input_file) as f:
    lines = f.readlines()

a = [int(i) for i in lines[1].strip().split()]
b = [int(i) for i in lines[3].strip().split()]

def merge_sort(a, b, c = []):
    len_a = len(a)
    len_b = len(b)
    while(len(c) != len_a + len_b):
        if a and b:
            if a[0] < b[0]:
                c = c + [a[0]]
                a = a[1:]
            else:
                c = c + [b[0]]
                b = b[1:]
        elif a and not b:
            c = c + [a[0]]
            a = a[1:]
        elif b and not a:
            c = c + [b[0]]
            b = b[1:]
    return c

result = merge_sort(a, b)
#print(' '.join([str(i) for i in result]))
