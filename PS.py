from HEA import build_binary_max_heap

input_file = 'Data/rosalind_ps.txt'
with open(input_file) as f:
    lines = f.readlines()
a = [int(i) for i in lines[1].strip().split()]
k = int(lines[2].strip())

max_heap = build_binary_max_heap(a[:k])
for i in range(k, len(a)):
    if a[i] < max_heap[0]:
        lst = max_heap[1:]
        lst.append(a[i])
        max_heap = build_binary_max_heap(lst)

max_heap.sort()
print(' '.join([str(i) for i in max_heap]))
