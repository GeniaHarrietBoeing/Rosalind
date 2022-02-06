input_file = 'Data/rosalind_fibo.txt'
with open(input_file) as f:
    lines = f.readlines()
lines = [i.strip() for i in lines]
n = int(lines[0])

F_0 = 0
F_1 = 1
for i in range(1, n):
    F = F_0 + F_1
    F_0 = F_1
    F_1 = F

print(F)
    
