import numpy as np

input_file = 'Data/rosalind_cte.txt'
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

shortest_cycle_dist = []
for g in graphs:
    edges = [[int(j) for j in i.strip().split()] for i in g]
    n = edges[0][0]
    nr_edges = edges[0][1]

    initial_node = edges[1][1]
    G = np.zeros((n+1,n+1))
    for i in range(1, len(edges)):
        G[edges[i][0], edges[i][1]] = edges[i][2]

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

    shortest_cycle_first_edge = edges[1][2] + dist[edges[1][0]]
    shortest_cycle_dist.append(shortest_cycle_first_edge)


shortest_cycle_dist = [str(int(i)) if i != np.inf else '-1' for i in shortest_cycle_dist]
print(' '.join(shortest_cycle_dist))
