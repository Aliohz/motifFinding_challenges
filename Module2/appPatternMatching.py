### Approximate Pattern Matching Problem: Find all approximate occurrences of a pattern in a string.

### Input: Strings Pattern and Text along with an integer d.
### Output: All starting positions where Pattern appears as a substring of Text with at most d mismatches.

# Variables
pattern = "CCC"
genome = "CATGCCATTCGCATTGTCCCAGTGA"
hD = 2 # Hamming Distance
k = len(pattern)
n = len(genome) + 1

subgenome = ""
startingPosition = []

# Calculate the hamming Distance
def hammingDistance(subgenome, pattern, hD):
    count = 0
    for i in range(k):
        if subgenome[i] != pattern[i]:
            count += 1
        #elif count > hD:
        #    break

    return count

for nucleotidePos in range(n - k):
    
    # Extracting sequences that match pattern lenght
    if nucleotidePos == 0:
        for i in range(k):
            subgenome += genome[i]
        calculated_hD = hammingDistance(subgenome, pattern, hD)
        
    else:
        i = nucleotidePos + k - 1

        subgenome = subgenome[1:]
        subgenome += genome[i]
        calculated_hD = hammingDistance(subgenome, pattern, hD) ## Room for improvement

    # Checking if sequences match the hamming Distance
    if calculated_hD <= hD:
        startingPosition.append(nucleotidePos)

#for i in startingPosition:
#    print(i, end= " ")

print(len(startingPosition))