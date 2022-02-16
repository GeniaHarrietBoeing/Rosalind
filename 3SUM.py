input_file = 'Data/rosalind_3sum.txt'
#input_file = 'Data/rosalind_3sum_1_dataset.txt'
with open(input_file) as f:
    lines = f.readlines()
lines = [[int(i) for i in j.strip().split()] for j in lines]
def dict_3SUM_approach(lines):
    result = []

    for a in lines[1:]:
        found_2sum = False
        sum2 = {}
        for i in range(0, len(a)-1):
            for j in range(i+1, len(a)):
                if a[i] + a[j] in sum2.keys():
                    sum2[a[i] + a[j]].append([i, j])
                else:
                    sum2[a[i] + a[j]] = [[i, j]] 
        for i in range(0, len(a) - 2):
            if -a[i] in sum2.keys():
                for k in sum2[-a[i]]:
                    if i not in k:
                        result.append([i+1, k[0]+1, k[1]+1])
                        found_2sum = True
                        break
            if found_2sum: break
        if not found_2sum:
            result.append([-1])
    return result


def presort_3SUM_approach(lines):
    result = []
    for a in lines[1:]:
        original_order = a.copy()
        a.sort()
        found_3sum = False
        for i in range(0, len(a)-2):
            if not found_3sum:
                start = i + 1
                end = len(a) - 1
                while end > start:
                    sum3 = a[start] + a[end]
                    if sum3 == -a[i]:
                        found_3sum = True
                        
                        #find original indexes:
                        original_indexes = []
                        for idx in [i, start, end]:
                            found = False
                            for j in range(0, len(original_order)):
                                if original_order[j] == a[idx] and found == False and j+1 not in original_indexes:
                                    found = True
                                    original_indexes.append(j+1)
                                    break
                                 
                        result.append(original_indexes)
                        break
                    elif sum3 + a[i] > 0:
                        end -= 1
                    elif sum3 + a[i] <= 0:
                        start += 1
        if not found_3sum:
            result.append([-1])
    return result
                
    
#result = dict_3SUM_approach(lines)
#for i in result:
#    i.sort()
#    print(' '.join([str(j) for j in i]))

result = presort_3SUM_approach(lines)
for i in result:
    i.sort()
    print(' '.join([str(j) for j in i]))
