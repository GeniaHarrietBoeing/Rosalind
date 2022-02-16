input_file = 'Data/rosalind_hea.txt'
with open(input_file) as f:
    lines = f.readlines()

a = [int(i) for i in lines[1].strip().split()]

def build_binary_max_heap(a):
    bin_heap = []
    for i in range(0, len(a)):
        bin_heap.append(a[i])
        k = i
        while k >= 1:
            parent_node = (k-1)//2
            if bin_heap[parent_node] <  bin_heap[k]:
                tmp = bin_heap[parent_node]
                bin_heap[parent_node] = a[i]
                bin_heap[k] = tmp
                k = parent_node
            else: 
                break
    return bin_heap

print(' '.join([str(i) for i in build_binary_max_heap(a)]))
            
