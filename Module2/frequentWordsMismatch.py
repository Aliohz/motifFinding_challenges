### Code Challenge: Solve the Frequent Words with Mismatches Problem.

### Input: A string Text as well as integers k and d. (You may assume k ≤ 12 and d ≤ 3.)
### Output: All most frequent k-mers with up to d mismatches in Text.

genome = "ACTACTTATCTCACTCTCCTCTATAATATACTAAGTAACTGTAACTCTCAATATACTTATACTTATAAACTACTACTAACTCCTCACTGTAACTTATCTCTATAAGTAGTATATTATTATTATACTACTCTCAATATCTCACTGTACTCTATACTTATACTGTATATCTCGTACTCAATATAAAAAAACTAAAAAAGTAACTAAACTGTAGTAAAGTAGTACTCCTC"
k = 6
d = 3
n = len(genome) + 1
reverseComplements = []

def extractSequence(genome, sequence_lenght, startingPoint):
    sequence = ""

    for i in range(startingPoint, startingPoint + sequence_lenght):
        sequence += genome[i]

    return sequence


def neighbors(pattern, d):
    if d == 0:
        return {pattern}
    
    neighborhood = set()
    neighborhood.add(pattern)

    for i in range(len(pattern)):
        for nucleotide in "ACGT":
            if nucleotide != pattern[i]:
                new_pattern = pattern[:i] + nucleotide + pattern[i+1:]
                
                for neighbor in neighbors(new_pattern, d - 1):
                    neighborhood.add(neighbor)

    return neighborhood
    

def maxDict(frequencyTable):
    max = 0

    for kmer in frequencyTable:
        if frequencyTable[kmer] > max:
            max = frequencyTable[kmer]

    return max


def frequentWordsMismatches(genome, k, d):
    patterns = []
    freqMap = {}
    n = len(genome) + 1

    for i in range(n-k):
        pattern = extractSequence(genome, k, i)
        neighborhood = neighbors(pattern, d)
        neighborhood = list(neighborhood)

        m = len(neighborhood)

        for x in range(m):
            reverse = reverseComplement(neighborhood[x])
            neighborhood.append(reverse)
        
        for j in range(len(neighborhood)):
            neighbor = neighborhood[j]

            if neighbor not in freqMap:
                freqMap[neighbor] = 1
            else:
                freqMap[neighbor] = freqMap[neighbor] + 1
        
    max = maxDict(freqMap)

    for pattern in freqMap:
        if freqMap[pattern] == max:
            patterns.append(pattern)

    return patterns


# Reverse complement
def reverseComplement(pattern):
    n = len(pattern) + 1
    reverseComplement = ""

    for nucleotide in range(-1, -abs(n), -1):
        if pattern[nucleotide] == "T":
            reverseComplement += "A"
        elif pattern[nucleotide] == "A":
            reverseComplement += "T"
        elif pattern[nucleotide] == "C":
            reverseComplement += "G"
        elif pattern[nucleotide] == "G":
            reverseComplement += "C"

    return reverseComplement


# Main
result = frequentWordsMismatches(genome, k, d)

for i in result:
    print(i, end= " ")