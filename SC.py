input_file = 'Data/rosalind_sc.txt'
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

def collapsed_scc(A, ts):
    lst_scc = []
    visited = [False] * len(A)
    visited[0] = True
    while(sum(visited) != len(visited)):
        tmp_visited = visited.copy()
        next_node = 0
        for i in ts:
            if not visited[i]:
                next_node = i
                break
        visited = scc_explore(A, next_node, ts, visited)    
        scc = [i for i in range(0, len(A)) if visited[i] and not tmp_visited[i]]
        lst_scc.append(scc)
    scc_dag = [[0]*(len(lst_scc)+1) for i in range(0, len(lst_scc)+1)]
    for i in range(0, len(lst_scc)):
        for j in lst_scc[i]:
            for n in range(0, len(lst_scc)):
                if n != i:
                    for k in lst_scc[n]:
                        if A[j][k] == 1:
                            scc_dag[i+1][n+1] = 1
    return scc_dag
    
def connections_scc(scc_dag, ts):
    for i in range(0, len(ts)-1):
        if scc_dag[ts[i]][ts[i+1]] != 1:
            return -1
    return 1

result = []
for g in graphs:
    A = adjacency_matrix(g)
    ts = topological_sort(A)
    A_r = reverse_graph(g) 
    scc_dag = collapsed_scc(A_r, ts)
    ts = topological_sort(scc_dag)
    result.append(connections_scc(scc_dag, ts))

print(' '.join([str(i) for i in result]))
