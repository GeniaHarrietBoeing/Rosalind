input_file = 'Data/rosalind_bins.txt'
with open(input_file) as f:
    lines = f.readlines()
lines = [i.strip().split() for i in lines]

n = int(lines[0][0])
m = int(lines[1][0])
A = [int(i) for i in lines[2]]
B = [int(i) for i in lines[3]]
def bin_search(array, n, x):
    start = 0
    end = n - 1
    while (end - start >= 0):
        middle = start + (end - start)//2
        if array[middle] == x:
            return middle
        else:
            if array[middle] > x:
                end = middle - 1 
            else:
                start = middle + 1
    return -1
         
result = []
for b in B:
    idx = bin_search(A, n, b)
    if idx != -1:
        idx += 1
    result += [str(idx)]


print(' '.join(result))

