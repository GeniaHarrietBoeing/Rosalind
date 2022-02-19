import random

input_file = 'Data/rosalind_med.txt'
with open(input_file) as f:
    lines = f.readlines()

a = [int(i) for i in lines[1].strip().split()]
k = int(lines[2].strip())

def find_k_smallest(a, k):
    while(True):
        rdm_idx = random.randint(0, len(a) - 1)
        smaller = []
        equal = 0
        larger = []
        
        for i in range(0, len(a)):
            if a[i] < a[rdm_idx]:
                smaller.append(a[i])
            elif a[i] == a[rdm_idx]:
                equal += 1
            elif a[i] > a[rdm_idx]:
                larger.append(a[i])
    
        if k <= len(smaller):
            a = smaller
        elif k <= len(smaller) + equal:
            return a[rdm_idx]
        elif k <= len(smaller) + equal + len(larger):
            a = larger
            k -= (len(smaller) + equal)

result = find_k_smallest(a, k)
print(result)
 
