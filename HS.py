from HEA import build_binary_max_heap

input_file = 'Data/rosalind_hs.txt'
with open(input_file) as f:
    lines = f.readlines()

a = [int(i) for i in lines[1].strip().split()]
bin_max_heap = build_binary_max_heap(a)


class bin_max_heap:
    def __init__(self, a):
        self.bin_max_heap = build_binary_max_heap(a) 

    def heap_sort(self):
        end = len(self.bin_max_heap) - 1
        while end >= 1:
            tmp = self.bin_max_heap[0]
            self.bin_max_heap[0] = self.bin_max_heap[end]
            self.bin_max_heap[end] = tmp
            end -= 1
            self.heapify(0, end + 1)

    def heapify(self, i, end):
        left = 2*i + 1
        right = 2*i + 2
        largest = i 
        if left < end and self.bin_max_heap[left] > self.bin_max_heap[largest]:
            largest = left   
        if right < end and self.bin_max_heap[right] > self.bin_max_heap[largest]:
            largest = right
        if largest != i:
            tmp = self.bin_max_heap[i]
            self.bin_max_heap[i] = self.bin_max_heap[largest]
            self.bin_max_heap[largest] = tmp    
            self.heapify(largest, end)


heap = bin_max_heap(a)
heap.heap_sort()
print(' '.join([str(i) for i in heap.bin_max_heap]))
