import numpy as np

input_file = 'Data/rosalind_sdag.txt'
with open(input_file) as f:
    lines = f.readlines()

lines = [[int(j) for j in i.strip().split()] for i in lines]
n = lines[0][0]
nr_edges = lines[0][1]

initial_node = 1
G = np.zeros((n+1,n+1))
for i in range(1, len(lines)):
    G[lines[i][0], lines[i][1]] = lines[i][2]
edges = lines[1:]
dist = [np.inf]*(n+1)
dist[initial_node] = 0

updates_this_round = True
for i in range(n - 1):

    if updates_this_round:
        updates_this_round = False

        for e in range(0, nr_edges):
            u = edges[e][0]
            v = edges[e][1] 

            if dist[v] > dist[u] + G[u][v]:
                updates_this_round = True
            dist[v] = min(dist[v], dist[u] + G[u][v])


dist = [str(int(dist[i])) if dist[i] != np.inf else 'x' for i in range(0, len(dist))]
print(' '.join(dist[1:]))

