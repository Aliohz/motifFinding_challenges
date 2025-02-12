# Given a lenght k, identifies the most frequent sequence or sequences within a given genome using a dictionary and iterating just once the genome

text = "CCCACGCACCCCACGCACCCTATCCACACTAAGGAATCGTGGGAATCGTGGGAATCGTGGGAATCGTGGCACTAAGGAATCGTGGCCCACGCACCCTATCCACCCACGCACCCCACGCACCCCACGCACCACTAAGCCTATCCACACTAAGTCGCCGCTCGCCGCCACTAAGGAATCGTGGTCGCCGCTCGCCGCTCGCCGCCACTAAGCCTATCCATCGCCGCTCGCCGCCCTATCCACCCACGCACCACTAAGCCCACGCACGAATCGTGGCACTAAGCACTAAGCCCACGCACCACTAAGTCGCCGCCCCACGCACCCCACGCACCACTAAGCCTATCCAGAATCGTGGTCGCCGCCCCACGCACCCCACGCACCACTAAGGAATCGTGGGAATCGTGGCCTATCCACACTAAGCCTATCCAGAATCGTGGCCTATCCAGAATCGTGGCCTATCCACACTAAGCACTAAGCCTATCCAGAATCGTGGCCCACGCACTCGCCGCCACTAAGTCGCCGCCCTATCCATCGCCGCCCTATCCATCGCCGCCCCACGCACGAATCGTGGCACTAAGCCCACGCACGAATCGTGGGAATCGTGGTCGCCGCGAATCGTGGTCGCCGCCCTATCCACCTATCCAGAATCGTGGCCCACGCACTCGCCGCGAATCGTGGCACTAAGTCGCCGCGAATCGTGGCCTATCCAGAATCGTGGTCGCCGCTCGCCGCCCCACGCACCACTAAGCCTATCCACACTAAGCCTATCCACACTAAGCCTATCCACCCACGCAC"
k = 13

# Creates the frequence table for all possible patterns using a dictionary
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

# Selects the max value or values from the dictionary
def maxDict(frequencyTable):
    max = 0

    for kmer in frequencyTable:
        if frequencyTable[kmer] > max:
            max = frequencyTable[kmer]

    return max

# Principal function
def freqWordsList(text, k):
    frequentPatterns = []
    frequencyTable = frequency(text, k)
    max = maxDict(frequencyTable)

    for kmer in frequencyTable:
        if frequencyTable[kmer] == max:
            frequentPatterns.append(kmer)

    return frequentPatterns

# Main
result = freqWordsList(text, k)
print(result)