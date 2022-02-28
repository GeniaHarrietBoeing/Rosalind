input_file = 'Data/rosalind_scc.txt'

with open(input_file) as f:
    lines = f.readlines()
lines = [[int(i) for i in j.strip().split()] for j in lines]

graph = []
for i in range(0, len(lines)):
    graph.append(lines[i])

def adjacency_matrix(graph):
    A = [[0]*(graph[0][0] + 1) for i in range(0, graph[0][0] + 1)]
    for e in graph[1:]:
        A[e[0]][e[1]] = 1
    return A

def reverse_graph(graph): 
    A = [[0]*(graph[0][0] + 1) for i in range(0, graph[0][0] + 1)]
    for e in graph[1:]:
        A[e[1]][e[0]] = 1
    return A

def DFS(A):
    counter = 0
    post = [0] * len(A)
    visited = [False] * len(A)
    for i in range(1, len(visited)):
        if not visited[i]:
            visited, counter, post = explore(A, visited, i, counter, post)

    return post

def explore(A, visited, i, counter, post):
    visited[i] = True
    for j in range(1, len(A)):
        if A[i][j] == 1 and not visited[j]:
            visited, counter, post = explore(A, visited, j, counter, post)
    counter += 1
    post[i] = counter
    return visited, counter, post

def scc_explore(A, i, ts, visited):
    visited[i] = True
    for j in ts:
        if A[i][j] == 1 and not visited[j]:
            visited = scc_explore(A, j, ts, visited)
    return visited

def topological_sort(A):
    post = DFS(A)
    result = []
    max_post = len(A) - 1
    while(max_post > 0):
        for i in range(1, len(post)):
            if post[i] == max_post:
                result.append(i)
                max_post -= 1
    return result

def count_scc(A, ts):
    count = 0
    visited = [False] * len(A)
    visited[0] = True
    while(sum(visited) != len(visited)):
        next_node = 0
        for i in ts:
            if not visited[i]:
                next_node = i
                break
        visited = scc_explore(A, next_node, ts, visited)
        count += 1

    return count
result = []
A = adjacency_matrix(graph)
ts = topological_sort(A)
A_r = reverse_graph(graph) 
print(count_scc(A_r, ts))





