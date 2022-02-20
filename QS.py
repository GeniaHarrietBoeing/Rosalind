input_file = 'Data/rosalind_qs.txt'
with open(input_file) as f:
    lines = f.readlines()
a = [int(i) for i in lines[1].strip().split()]
def quick_sort(start, end):
   if start < end:
        pivot = partition(start, end)
        quick_sort(start, pivot - 1)
        quick_sort(pivot + 1, end)

    

def partition(start, end):
    i = start   
    j = end - 1
    pivot = a[end]

    while i < j:
        while i < end and a[i] < pivot:
            i += 1

        while j > start and a[j] >= pivot:
            j -= 1

        if i < j:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp

    if a[i] > pivot:
        tmp = a[i]
        a[i] = a[end]
        a[end] = tmp
    
    return i
        
quick_sort(0, len(a) - 1)
print(' '.join([str(i) for i in a]))     
