input_file = 'Data/rosalind_inv.txt'
with open(input_file) as f:
    lines = f.readlines()
a = [int(i) for i in lines[1].strip().split()]

def counting_inversions(a): 
    nr_inversions = 0
    for i in range(0, len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                nr_inversions += 1
    return nr_inversions

result = counting_inversions(a)
print(result)
