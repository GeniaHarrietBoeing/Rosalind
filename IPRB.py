input_file = 'Data/rosalind_iprb.txt'
with open(input_file) as f:
    data = f.read()
data = data.strip().split()
k = int(data[0])
m = int(data[1])
n = int(data[2])
tot = k + m + n

# the 2* because there are 2 ways of doing k x n
prob_dominant = k * (k-1) + 0.75*m*(m-1) + 2*(k*n + k*m + 0.5*m*n)
prob_dominant /= (tot * (tot - 1))
print(prob_dominant)
print(k, m, n, tot)
