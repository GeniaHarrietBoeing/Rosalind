input_file = 'Data/rosalind_fib.txt'
with open(input_file) as f:
    data = f.read()

data = data.strip().split(' ')
n = int(data[0])
k = int(data[1])

print('n, k:    ', n, k)

F = [1, 1, 0]

# F[0] are all the reproducing rabbits
# F[1] are all the rabbits present in previous month
for i in range(2, n):

    F[2] = F[0]*k + F[1]

    F[0] = F[1]
    F[1] = F[2]

print('number of rabbits in month n:    ', F[2])
