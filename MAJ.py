input_file = 'Data/rosalind_maj.txt'
with open(input_file) as f:
    lines = f.readlines()

lines = [[int(i) for i in j.strip().split()] for j in lines]

def get_majority_element(a):
    
    return get_majority(a, 0, len(a) - 1)

def get_majority(a, l, r):
    if l == r:
        return a[l]
    
    mid = (r-l)//2 + l
    left_majority = get_majority(a, l, mid)
    right_majority = get_majority(a, mid+1, r)

    if left_majority == right_majority:
        return left_majority
    
    nr_left_majority = 0
    nr_right_majority = 0
    for i in a:
        if i == left_majority: nr_left_majority += 1
        if i == right_majority: nr_right_majority += 1

    if nr_left_majority > nr_right_majority and nr_left_majority >= len(a)//2+1: 
        return left_majority
    elif nr_right_majority > nr_left_majority and nr_right_majority >= len(a)//2+1: 
        return right_majority
    else:
        return -1
    
result = []
for a in lines[1:]:
    result += [str(get_majority_element(a))]

print(' '.join(result))
