input_file = 'Data/rosalind_bfs.txt'
with open(input_file) as f:
    lines = f.readlines()

graph = []
for l in range(0, len(lines)):
    graph.append([int(i) for i in lines[l].strip().split()])

def adjacency_matrix(graph):
    A = [[0]*(graph[0][0] + 1) for i in range(0, graph[0][0] + 1)]
    for e in graph[1:]:
        A[e[0]][e[1]] = 1
    return A


def bfs(A, starting_node):
    dist = [-1] * len(A)
    dist[starting_node] = 0
    queue = [starting_node]

    while(queue):
        node = queue.pop(0)
        for i in range(0, len(A)):
            if A[node][i] == 1 and dist[i] == -1: 
                queue.append(i)
                dist[i] = dist[node] + 1
    return dist[1:]

starting_node = 1
A = adjacency_matrix(graph)
result = bfs(A, starting_node)
print(' '.join([str(i) for i in result]))
