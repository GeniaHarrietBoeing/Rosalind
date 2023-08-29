input_file = 'Data/rosalind_ba1c.txt'
with open(input_file) as f:
    data = f.read()
data = data.strip()


complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

def getReverseComplement(data):
    reverse = [0] * len(data)
    
    for i in range(0, len(data)):
        reverse[-i - 1] = complement[data[i]]

    reverseStrand = ''
    return reverseStrand.join(reverse)

print(getReverseComplement(data))
