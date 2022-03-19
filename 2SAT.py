import sys

input_file = 'Data/rosalind_2sat.txt'
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
    nr_nodes = graph[0][0]
    A = [[0]*(nr_nodes*2 + 1) for i in range(0, nr_nodes*2 + 1)]
    for e in graph[1:]: 
        A[e[0]*(-1) + nr_nodes][e[1] + nr_nodes] = 1
        A[e[1]*(-1) + nr_nodes][e[0] + nr_nodes] = 1
    return A

def reverse_matrix(graph): 
    nr_nodes = graph[0][0]
    A = [[0]*(nr_nodes*2 + 1) for i in range(0, nr_nodes*2 + 1)]
    for e in graph[1:]: 
        A[e[1] + nr_nodes][e[0]*(-1) + nr_nodes] = 1
        A[e[0] + nr_nodes][e[1]*(-1) + nr_nodes] = 1
    return A

def DFS(A):
    counter = 0
    post = [0] * len(A)
    visited = [False] * len(A)
    visited[len(A)//2] = True
    for i in range(0, len(visited)):
        if not visited[i]:
            visited, counter, post = explore(A, visited, i, counter, post)
    return post

def explore(A, visited, i, counter, post):
    visited[i] = True
    for j in range(0, len(A)):
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
    while(max_post >= 0):
        for i in range(0, len(post)):
            if post[i] == max_post:
                result.append(i)
                max_post -= 1
    return result

def scc(A, ts):
    lst_scc = []
    visited = [False] * len(A)
    visited[len(A)//2] = True
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
    return lst_scc

def is_2sat(lst_scc, nr_nodes):
    for scc in lst_scc:
        for i in scc:
            original_node = i - nr_nodes
            negative_node = -1 * original_node
            offset_negative_node = negative_node + nr_nodes

            if (offset_negative_node) in scc:
                return 0
    return 1

def find_2sat(lst_scc, A):
    scc_dag = collapsed_scc(A, lst_scc)
    ts = topological_sort(scc_dag)
    assigned = [False] * len(A)
    assigned[len(A)//2] = True
    valid_assignment = []
    while(sum(assigned) != len(assigned)):
        for i in range(0, len(ts)):
            scc = lst_scc[ts[i]]
            for n in scc:
                if not assigned[n]: 
                    assigned[n] = True
                    original_node = n - nr_nodes
                    negative_node = -1 * original_node
                    offset_negative_node = negative_node + nr_nodes
                    assigned[offset_negative_node] = True
                    valid_assignment.append(n)
    sorted_valid_assignment = [0] * (len(valid_assignment) + 1)
    for i in range(0, len(valid_assignment)):
        original_node = valid_assignment[i] - nr_nodes
        sorted_valid_assignment[abs(original_node)] = original_node
    return sorted_valid_assignment[1:]

def collapsed_scc(A, lst_scc):
    scc_dag = [[0]*(len(lst_scc)) for i in range(0, len(lst_scc))]
    for i in range(0, len(lst_scc)):
        for j in lst_scc[i]:
            for n in range(0, len(lst_scc)):
                if n != i:
                    for k in lst_scc[n]:
                        if A[j][k] == 1:
                            scc_dag[i][n] = 1
    return scc_dag

def check_assignment(graph, assignment):
    for i in graph[1:]:
        if not i[0] in assignment and not i[1] in assignment:
            print(i[0], i[1], len(assignment))
            return False
    return True

result = []
for g in graphs:
    nr_nodes = g[0][0]
    #the following feels incredibly dirty
    if nr_nodes*2 > 1000:
        sys.setrecursionlimit(nr_nodes*2 + 1)
    A = adjacency_matrix(g)
    A_r = reverse_matrix(g)
    ts = topological_sort(A)[:-1]
    lst_scc = scc(A_r, ts)
    sat = is_2sat(lst_scc, nr_nodes)
    if not sat:
        result.append([0])
    else:
        assignment = find_2sat(lst_scc, A_r)
        result.append([1] + assignment)
        print('does assignment work?    ', check_assignment(g, assignment))
for i in result:
    #print(' '.join([str(j) for j in i]))
    x = 1
