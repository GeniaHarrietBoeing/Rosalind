input_file = 'Data/rosalind_subs.txt'

with open(input_file) as f:
    data = f.readlines()
data = [i.strip() for i in data]
s = data[0]
t = data[1]


pos = ''
for i in range(0, len(s)):
    if s[i:i+len(t)] == t:
        pos +=str(i+1) + ' '
print(pos)

