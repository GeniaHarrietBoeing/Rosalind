input_file = 'Data/rosalind_dag.txt'
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
    A = [[0]*(len(graph) + 1) for i in range(0, len(graph) + 1)]
    for e in graph[1:]:
        A[e[0]][e[1]] = 1
    return A

def DFS(A):
    visited = [False]*len(A)
    visited[0] = True
    order = []
    for i in range(0, len(visited)):
        if not visited[i]:
            visited, order = explore(A, visited, order, i)
    return order

def explore(A, visited, order, i):
    visited[i] = True
    order.append(i)
    if sum(A[i]) != 0:
        for j in range(0, len(A)):
            if A[i][j] == 1 and not visited[j]:
                visited, order = explore(A, visited, order, j)
            elif A[i][j] == 1 and visited[j]:
                order.append(j)
                order.append(j)
    order.append(i)
    return visited, order

def is_acyclic(order):
    stack = [order[0]]
    for i in range(1, len(order)):
        if stack:
            
            if stack[-1] == order[i]:
                stack.pop()
            elif order[i] in stack:
                return -1
            else:
                stack.append(order[i])
    if not stack:
        return 1

result = []
for g in graphs:
    A = adjacency_matrix(g)
    order = DFS(A)
    result.append(is_acyclic(order))

print(' '.join([str(i) for i in result]))
