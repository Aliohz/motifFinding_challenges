### Clump Finding Problem: Find patterns forming clumps in a string.
### Input: A string Genome, and integers k, L, and t.
### Output: All distinct k-mers forming (L, t)-clumps in Genome.

file = open(r"C:\Users\Abn3r\Documents\PythonProjects\Bioinformatics\Module1\E_coli.txt", "r")
genome = file.read()
k, L, t = 9, 500, 3

def findClumps(genome, k, L, t):
    
    patterns = []
    n = len(genome) + 1

    for i in range(0, n - L):
        window = extractSequence(genome, L, i)
        frequencyTable = frequency(window, k)

        for kmer in frequencyTable:
            if frequencyTable[kmer] >= t:
                if kmer not in patterns:
                    patterns.append(kmer)
    
    return patterns

def extractSequence(genome, sequence_lenght, startingPoint):
    sequence = ""

    for i in range(startingPoint, startingPoint + sequence_lenght):
        sequence += genome[i]

    return sequence

def frequency(text, k):
    freqDict = {}
    n = len(text) + 1

    for i in range(0, n - k):
        pattern = ""
        for j in range(0, k):
              pattern += text[i + j]
    
        if pattern not in freqDict:
            freqDict[pattern] = 1
        else:
            freqDict[pattern] += 1

    return freqDict

patternClump = findClumps(genome, k, L, t)

for pattern in patternClump:
    print(pattern, end= " ")

print(len(patternClump))

file.close()