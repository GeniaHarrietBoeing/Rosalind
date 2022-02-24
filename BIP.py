input_file = 'Data/rosalind_bip.txt'
with open(input_file) as f:
    lines = f.readlines()
lines = [[int(i) for i in j.strip().split()] for j in lines]

graphs = []
for l in range(1, len(lines)):
    if not lines[l]:
        if l > 1:
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

def is_bipartite(A):    
    visited = [False] * len(A)
    visited[0] = True
    color = [False] * len(A)
    color[1] = True
    visited[1] = True
    bipartedness, visited, color = explore(A, visited, color, 1)
    if bipartedness == False:
        return -1
    return 1

def explore(A, visited, color, i):
        for j in range(1, len(A)):
            if i != j:
                if A[i][j] == 1 and not visited[j]:
                    visited[j] = True
                    color[j] = not color[i]
                    bipartedness, visited, color = explore(A, visited, color, j)
                    if(not bipartedness):
                        return False, visited, color
                    elif color[i] == color[j]:
                        return False, visited, color
                elif A[i][j] and visited[j]:
                    if color[i] == color[j]:
                        return False, visited, color
        return True, visited, color

result = []
for g in graphs:
    A = adjacency_matrix(g)
    result.append(is_bipartite(A))

print(' '.join([str(i) for i in result]))
