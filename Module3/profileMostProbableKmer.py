### Profile-most Probable k-mer Problem: Find a Profile-most probable k-mer in a string.

### Input: A string Text, an integer k, and a 4 × k matrix Profile.
### Output: A Profile-most probable k-mer in Text.

import numpy as np

dna = "CTGTTCGC"
k = 3
raw_profile = """
0.125 0.25 0.375
0.125 0.125 0.125
0.375 0.375 0.125
0.375 0.25 0.375
"""
# Convert the string to a NumPy matrix
profile = np.array([list(map(float, line.split())) for line in raw_profile.strip().split("\n")])

def kmerProbability(kmer, profile):
    profile_rows = {"A": 0, "C": 1, "G": 2, "T": 3}
    kmer_probability = 1

    for i in range(len(kmer)):
        row = profile_rows[kmer[i]]
        column = i
        nucleotide_probability = profile[row][column]
        kmer_probability *= nucleotide_probability
        
        if kmer_probability == 0:
            break

    return kmer_probability


def profile_most_probable_kmer(dna, k, profile):
    n = len(dna) + 1
    highestProbability = -1

    for i in range(n - k):
        kmer = dna[i:i+k]

        kmer_probability = kmerProbability(kmer, profile)

        if kmer_probability > highestProbability:
            highestProbability = kmer_probability
            most_probable_kmer = kmer
    
    return most_probable_kmer

most_probable_kmer = profile_most_probable_kmer(dna, k, profile)
print(most_probable_kmer)