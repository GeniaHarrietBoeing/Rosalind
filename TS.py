input_file = 'Data/rosalind_ts.txt'
with open(input_file) as f:
    lines = f.readlines()
lines = [[int(i) for i in j.strip().split()] for j in lines]

def adjacency_matrix(graph):
    A = [[0]*(graph[0][0] + 1) for i in range(0, graph[0][0] + 1)]
    for e in graph[1:]:
        A[e[0]][e[1]] = 1
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


A = adjacency_matrix(lines)
post = DFS(A)

result = []
max_post = len(A) - 1
while(max_post > 0):
    for i in range(1, len(post)):
        if post[i] == max_post:
            result.append(i)
            max_post -= 1

print(' '.join([str(i) for i in result]))

