input_file = 'Data/rosalind_iev.txt'
with open(input_file) as f:
    data = f.read()
data = data.strip().split()
data = [int(i) for i in data]

tot = sum(data) * 2
dominant = data[0] * 2
dominant += data[1] * 2
dominant += data[2] * 2
dominant += data[3] * 3/4 * 2
dominant += data[4] * 1

print(dominant)
