### Code Challenge: Implement MedianString.

### Input: An integer k, followed by a space-separated collection of strings Dna.
### Output: A k-mer Pattern that minimizes d(Pattern, Dna) among all possible choices of k-mers. (If there are multiple such strings Pattern, then you may return any one.)

dna = '''
CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC
GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC
GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG
'''
dna = dna.split()
k = 7

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


def hammingDistance(genome1, genome2):

    n = len(genome1)
    count = 0

    for i in range(n):
        if genome1[i] != genome2[i]:
            count += 1

    return count


def distance(pattern, dna):
    k = len(pattern)
    sum_hD = 0
    
    for string in dna:

        distance = k

        for i in range(len(string) - k + 1):
            kmer = string[i:i+k]
            hD = hammingDistance(pattern, kmer)

            if hD < distance:
                distance = hD

        sum_hD += distance

    return sum_hD


def medianString(dna, k):
    d = k * len(dna)
    neighborhood = neighbors("A" * k, k)

    for pattern in neighborhood:

        current_distance = distance(pattern, dna)

        if d >= current_distance:
            d = current_distance
            print(f"d: {d}")
            median = pattern
            print(f"median: {median}")
            
    
    return median

consensus = medianString(dna, k)
print(consensus)