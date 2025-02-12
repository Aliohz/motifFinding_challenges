### Code Challenge: Implement MotifEnumeration (reproduced below).

### Input: Integers k and d, followed by a space-separated collection of strings Dna.
### Output: All (k, d)-motifs in Dna.

dna = "ACTCTTGGGTTCTGTAACATTCAAC GAGCGTTACGCTCGGCAGTATCAAT CTTTATCAAAAGGTCCAAGGGAGTT CCCCGGTCGAGAGGATCAACTCTTT ATTCATCAACCTAGTGGGGAACGCT GATGGCTAGGACGGTTCAACAAAAA"
dna = dna.split()
k = 5
d = 1


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


def motifEnumeration(dna, k, d):
    patterns = set()

    n = len(dna[0]) + 1
    m = len(dna)

    for i in range(n - k):
        sequence = dna[0]
        pattern = sequence[i:i + k]

        for neighbor in neighbors(pattern, d):

            count = 0
            for j in range(1, m):
                sequence = dna[j]

                for x in range(n - k):

                    kmer = sequence[x:x + k]

                    if hammingDistance(neighbor, kmer) <= d:
                        count += 1
                        break
                
                if count == (m - 1):
                    patterns.add(neighbor)

    return patterns


motifs = motifEnumeration(dna, k, d)

for motif in motifs:
    print(motif, end= " ")