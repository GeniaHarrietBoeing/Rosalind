import numpy as np

input_file = 'Data/rosalind_dij.txt'
with open(input_file) as f:
    lines = f.readlines()

lines = [[int(j) for j in i.strip().split()] for i in lines]
n = lines[0][0]
nr_edges = lines[0][1]

initial_node = 1
G = np.zeros((n+1,n+1))
for i in range(1, len(lines)):
    G[lines[i][0], lines[i][1]] = lines[i][2]

dist = [np.inf]*(n+1)
dist[initial_node] = 0
Q = [i for i in range(1, n+1)]

while(Q):
    u = Q[0]

    for q in Q:
        if dist[q] < dist[u]:
            u = q

    for i in range(0, len(Q)):
        if Q[i] == u:
            Q.pop(i)
            break   

    for q in Q:
        if G[u][q] != 0:
            alt = dist[u] + G[u][q]
            if alt < dist[q]:
                dist[q] = alt

dist = [str(int(dist[i])) if dist[i] != np.inf else '-1' for i in range(0, len(dist))]
print(' '.join(dist[1:]))

