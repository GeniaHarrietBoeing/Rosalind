input_file = 'Data/rosalind_sq.txt'
with open(input_file) as f:
    lines = f.readlines()
lines = [[int(i) for i in j.strip().split()] for j in lines]

graphs = []
for l in range(1, len(lines)):
    if not lines[l]:
        if l != 1:
            graphs.append(graph)
        graph = []
    else:
        graph.append(lines[l])
graphs.append(graph)

def adjacency_matrix(graph):
    A = [[0]*(graph[0][0] + 1) for i in range(0, graph[0][0] + 1)]
    for i in graph[1:]:
        A[i[0]][i[1]] = 1
        A[i[1]][i[0]] = 1   
    return A
    
def contains_square(A):
    for i in range(1, len(A)-1):
        for j in range(i+1, len(A)):
                common_node = 0
                for k in range(1, len(A)):  
                    if A[i][k] == 1 and A[j][k] == 1:
                        common_node += 1
                if common_node >= 2:
                    return 1
    return -1


result = []
for g in graphs:
    A = adjacency_matrix(g)
    result.append(contains_square(A))    

print(' '.join([str(i) for i in result]))
