input_file = 'Data/rosalind_ins.txt'
with open(input_file) as f:
    lines = f.readlines()

lines = [i.strip() for i in lines]
n = int(lines[0])
A = [int(i) for i in lines[1].split()]

def insertionSort(A):
    counter_swaps = 0
    for i in range(1, len(A)):
        k = i
        while (k > 0 and A[k] < A[k-1]):
            tmp = A[k-1]
            A[k-1] = A[k]
            A[k] = tmp
            k -= 1
            counter_swaps += 1
    print(counter_swaps)
    return A

insertionSort(A)
