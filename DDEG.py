input_file = 'Data/rosalind_ddeg.txt'
with open(input_file) as f:
    lines = f.readlines()
lines = [[int(i) for i in j.strip().split()] for j in lines]
edges = lines[1:]
nr_nodes = lines[0][0]
nr_edges = lines[0][1]

degrees = [0] * (nr_nodes + 1)
for i in range(1, nr_nodes + 1):
    for e in edges:
        if i in e:
            degrees[i] += 1
neighbours = [0] * (nr_nodes + 1)

for i in range(1, nr_nodes + 1):
    nodes = []
    for e in edges:
        if e[1] == i:   
            nodes.append(e[0])
        elif e[0] == i: nodes.append(e[1])
    neighbours[i] = nodes

result = []
for i in range(1, nr_nodes + 1):
    double_degree = 0
    for n in neighbours[i]:
        double_degree = sum([degrees[j] for j in neighbours[i]])
    result += [str(double_degree)]

print(' '.join(result))
