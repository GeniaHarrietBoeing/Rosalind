input_file = 'Data/rosalind_deg.txt'
with open(input_file) as f:
    lines = f.readlines()
lines = [i.strip().split() for i in lines]
lines = lines[1:]
nodes = {}
for i in lines:
    if i[0] in nodes.keys():
        nodes[i[0]] += 1
    else:
        nodes[i[0]] = 1

    if i[1] in nodes.keys():
        nodes[i[1]] += 1
    else:
        nodes[i[1]] = 1
result = []
for i in range(1, len(nodes.keys())+1):
    if str(i)in list(nodes.keys()):
        result += [str(nodes[str(i)])]

print(' '.join(result))
