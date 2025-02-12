### Hamming Distance Problem: Compute the Hamming distance between two strings.

### Input: Two strings of equal length.
### Output: The Hamming distance between these strings.

genome1 = "CTACAGCAATACGATCATATGCGGATCCGCAGTGGCCGGTAGACACACGT"
genome2 = "CTACCCCGCTGCTCAATGACCGGGACTAAAGAGGCGAAGATTATGGTGTG"

def hammingDistance(genome1, genome2):

    n = len(genome1)
    count = 0

    for i in range(n):
        if genome1[i] != genome2[i]:
            count += 1

    return count

hD = hammingDistance(genome1, genome2)
print(hD)