import MER

input_file = 'Data/rosalind_ms.txt'
with open(input_file) as f:
    lines = f.readlines()

a = [int(i) for i in lines[1].strip().split()]

def merge_sort(a):
    if len(a) == 2:
        lst = [0] * 2
        lst[0] = min(a)
        lst[1] = max(a)
        return lst
    elif len(a) == 1:
        return a
    else:
        middle = len(a)//2
        half1 = merge_sort(a[:middle])
        half2 = merge_sort(a[middle:])
        merged = MER.merge_sort(half1, half2)
        return merged

result = merge_sort(a)
print(' '.join([str(i) for i in result]))
        
        
 
