import math
input_file = 'Data/rosalind_sign.txt'
with open(input_file) as f:
    lines = f.readlines()
n = int(lines[0])

def signed_permutation(p, n):

    if len(p) == n:
        print(' '.join([str(i) for i in p]))
    else:
        for i in range(-n, n+1):
            if i not in p and -i not in p and i != 0:
                signed_permutation( p + [i], n)

# there are n! permutations of the unsigned numbers, and there are 2**n permutations of {-1, 1, -1, -1, ...}
print(2**n * math.factorial(n))
signed_permutation([], n)
