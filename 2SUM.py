input_file = 'Data/rosalind_2sum.txt'
with open(input_file) as f:
    lines = f.readlines()
lines = [[int(i) for i in j.strip().split()] for j in lines]


result = [] 

for a in lines[1:]:
    sum2 = False
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            if a[i] == -a[j] and i != j:
                result.append([str(i+1), str(j+1)])
                sum2 = True
                break
        if sum2: break
    if sum2 == False:
        result.append([str(-1)])
        
for i in result:
    print(' '.join(i))
