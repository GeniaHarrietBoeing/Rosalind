input_file = 'Data/rosalind_fibd.txt'
with open(input_file) as f:
    data = f.read()
data = data.strip().split()
n = int(data[0])
m = int(data[1])

rabbits = [1]

# takes ages if n > 40
def reproduction_until_death(months_remaining, m):
    #one pair modelled:
    global rabbits
    for i in range(2, m + 1):
        if i == m and months_remaining - m > 0:
            rabbits.append(-1)
        if months_remaining - i > 0:
            rabbits.append(1)
            reproduction_until_death(months_remaining - i , m)




population_age = [0] * m 
population_age[0] = 1

def population_reproduction(n, m):
    global population_age
    for i in range(n-1):
        #first of all they all age, and die
        to_die = population_age[m-1]
        for j in range(m-1, 0, -1):
            population_age[j] = population_age[j-1]
        population_age[0] = 0
        population_age[0] = sum(population_age[2:]) + to_die
    
    print('nr_rabbits:  ', sum(population_age))

print('n, m ', n, m)
population_reproduction(n, m) 
