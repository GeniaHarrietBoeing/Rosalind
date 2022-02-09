input_file = 'Data/rosalind_tree.txt'
with open(input_file) as f:
    lines = f.readlines()
lines = [i.strip().split() for i in lines]
n = int(lines[0][0])
nodes = lines[1:]
nodes = [[int(i) for i in j] for j in nodes]

trees = []
for i in nodes:
    nodes_added = False
    for t in range(0, len(trees)):
        if i[0] in trees[t] and i[1] not in trees[t]:
            trees[t].append(i[1])
            nodes_added = True
        if i[1] in trees[t] and i[0] not in trees[t]:
            trees[t].append(i[0])
            nodes_added = True
    if not nodes_added:
        trees.append(i)

#Lonely nodes:
lonely_nodes = 0
for i in range(1, n + 1):
    lonely = True
    for nd in nodes:
        if nd[0] == i or nd[1] == i:
            lonely = False
    if lonely:
        lonely_nodes += 1

# Only had to do the following:
print(n - len(nodes) - 1)
