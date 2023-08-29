input_file = 'Data/rosalind_gs.txt'
with open(input_file) as f:
    lines = f.readlines()
lines = [[int(i) for i in j.strip().split()] for j in lines]

nr_graphs = lines[0][0]
graphs = []
for i in range(1, len(lines)):
    if not lines[i]:   
        if i != 1:
            graphs.append(graph)
        graph = []
    else:
        graph.append(lines[i])
graphs.append(graph)


def adjacency_matrix(graph):
    A = [[0]*(graph[0][0] + 1) for i in range(0, graph[0][0] + 1)]
    for e in graph[1:]:
        A[e[0]][e[1]] = 1
    return A

def explore(A, visited, i):
    visited[i] = True
    for j in range(1, len(A)):
        if not visited[j] and A[i][j] == 1:
            visited = explore(A, visited, j)
    return visited

def naive_check_general_sink(A):
    for i in range(1, len(A)):
        visited = [False] * len(A)
        visited[0] = True
        visited = explore(A, visited, i)
        if sum(visited) == len(visited):
            return i
    return -1



result = []
for g in graphs:
    A = adjacency_matrix(g)
    result.append(naive_check_general_sink(A))

print(' '.join([str(i) for i in result]))
