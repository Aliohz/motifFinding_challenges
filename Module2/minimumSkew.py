### Minimum Skew Problem: Find a position in a genome where the skew diagram attains a minimum.

### Input: A DNA string Genome.
### Output: All integer(s) i minimizing Skewi (Genome) among all values of i (from 0 to |Genome|).

genome = "CATTCCAGTACTTCGATGATGGCGTGAAGA"
skew = [0]
n = len(genome)

for i in range(n):
    if genome[i] == "C":
        skewValue = skew[i] - 1
        skew.append(skewValue)
    elif genome[i] == "G":
        skewValue = skew[i] + 1
        skew.append(skewValue)
    else:
        skewValue = skew[i]
        skew.append(skewValue)

minimum = min(skew)
minimumSkews = []

for i in range(len(skew)):
    if skew[i] == minimum:
        minimumSkews.append(i)

for i in minimumSkews:
    print(i, end= " ")