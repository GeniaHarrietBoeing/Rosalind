import numpy as np

input_file = 'Data/rosalind_nwc.txt'
with open(input_file) as f:
    lines = f.readlines()


graphs = []
g = []
for l in lines:
    if len([int(j) for j in l.strip().split()]) == 2:
        graphs.append(g)
        g =[l]
    else:
        g.append(l)
graphs.append(g)
graphs.pop(0)

negative_cycles = []
for g in graphs:
    g = [[int(j) for j in i.strip().split()] for i in g]
    n = g[0][0]+1 #+1 for dummy node
    nr_edges = 0
    # dummy source node connected to everything
    initial_node = 0
    G = np.zeros((n+1,n+1))
    for i in range(1, len(g)):
        G[g[i][0], g[i][1]] = g[i][2]
    edges = g[1:]
    dummy_edges = [[0, i, 0] for i in range(1, n)]
    edges += dummy_edges
    dist = [np.inf]*(n+1)
    dist[initial_node] = 0

    for i in range(n - 1):

        for e in range(0, len(edges)):
            u = edges[e][0]
            v = edges[e][1] 

            dist[v] = min(dist[v], dist[u] + G[u][v])

    # negative cycle detection
    negative_cycle = False

    for i in range(n-1):
        if not negative_cycle:
            for e in range(0, len(edges)):
                u = edges[e][0]
                v = edges[e][1] 
                if dist[u] + G[u][v] < dist[v]:
                    negative_cycle = True
            
    if negative_cycle:
        negative_cycles.append('1')
    else:
        negative_cycles.append('-1')
print(' '.join(negative_cycles))

