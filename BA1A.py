input_file = 'Data/rosalind_ba1a.txt'
with open(input_file) as f:
    lines = f.readlines()
lines = [i.strip() for i in lines]

text = lines[0]
pattern = lines[1]

pattern_count= 0
for i in range(0, len(text)-len(pattern)+1):
    if text[i:i+len(pattern)] == pattern: 
        pattern_count += 1
print(pattern_count)
