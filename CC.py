input_file = 'Data/rosalind_cc.txt'
with open(input_file) as f:
    lines = f.readlines()
lines = [[int(i) for i in j.strip().split()] for j in lines]
nr_nodes = lines[0][0]
nr_edges = lines[0][1]
edges = lines[1:]

A = [[0]*(nr_nodes + 1) for i in range(0, nr_nodes + 1)]
for e in edges:
    A[e[0]][e[1]] = 1
    A[e[1]][e[0]] = 1

visited = [False]*(nr_nodes + 1)
visited[0] = True

def DFS(A, visited):    
    nr_components = 0
    for i in range(0, len(visited)):
        if not visited[i]:
            nr_components += 1
            visited = explore(A, visited, i)
    return nr_components

def explore(A, visited, i):
    visited[i] = True
    if sum(A[i]) != 0:
        for j in range(0, len(A)):
            if A[i][j] == 1 and not visited[j]:
                visited = explore(A, visited, j)
    return visited

result = DFS(A, visited)
print(result)
