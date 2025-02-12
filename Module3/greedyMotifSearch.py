### Code Challenge: Implement GreedyMotifSearch.

### Input: Integers k and t, followed by a space-separated collection of strings Dna.
### Output: A collection of strings BestMotifs resulting from applying GreedyMotifSearch(Dna, k, t). If at any step you find more than one Profile-most probable k-mer in a given 
### string, use the one occurring first.

import numpy as np
import math

dna = '''
GACCTACGGTTACAACGCAGCAACCGAAGAATATTGGCAA
TCATTATCGATAACGATTCGCCGGAGGCCATTGCCGCACA
GGAGTCTGGTGAAGTGTGGGTTATGGGGCAGACTGGGAAA
GAATCCGATAACTGACACCTGCTCTGGCACCGCTCTCATC
AAGCGCGTAGGCGCGGCTTGGCATCTCGGTGTGTGGCCAA
AATTGAAAGGCGCATCTTACTCTTTTCGCTTAAAATCAAA
GGTATAGCCAGAAAGCGTAGTTAATTTCGGCTCCTGCCAA
TCTGTTGTTGCTAACACCGTTAAAGGCGGCGACGGCAACT
'''
dna = dna.split()
k = 5
t = 8


def buildProfile(motif_matrix, k):
    profile = np.zeros((4, k))
    profile_rows = {"A": 0, "C": 1, "G": 2, "T": 3}
    t = len(motif_matrix)
    
    for column in range(k):
        for motif_row in range(t):
            nucleotide = motif_matrix[motif_row][column]
            profile_row = profile_rows[nucleotide]

            profile[profile_row][column] += 1 / t

    return profile

'''
# This scoring is based in Entropy (H). Entropy is a measure of the uncertainty of a probability distribution. The lower the entropy, the better the profile to predict motifs.
def scoreProfile(profile):
    columns = len(profile[0])
    rows = len(profile)

    score = 0

    for column in range(columns):
        H = 0
        for row in range(rows):
            # -Minus sign is expressed here to sum values since all results are expected to be negative.
            a = profile[row][column]
            if a != 0: # Handles the log(0, 2) error
                H -= math.log(a, 2)
        
        score += H

    return score


# I only use this scoring function to get the problem right, however the Entropy function is more accurate in real life.
def scoreProfile(profile):
    columns = len(profile[0])
    rows = len(profile)

    score = 0

    for column in range(columns):
        frecuency = []
        for row in range(rows):
            a = profile[row][column]
            frecuency.append(a)

        inversed_max = 1 - max(frecuency) # It prevents having to edit code in the main function
        score += inversed_max

    return score
'''

# Third attempt to get the right score function for this exercise. It uses the motifs instead of the profile, take this into account when going back to the original code.
def score_motif_matrix(motif_matrix):
    columns = len(motif_matrix[0])
    rows = len(motif_matrix)

    score = 0

    for column in range(columns):
        frequency = ""
        for row in range(rows):
            a = motif_matrix[row][column]
            frequency += a
        
        max_count = max(frequency.count(nucleotide) for nucleotide in 'ACGT')
        score += rows - max_count

    return score


# Imported form profileMostProbableKmer.py
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


# Imported form profileMostProbableKmer.py
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


def greedy_motif_search(dna, k , t):
    n = len(dna[0]) + 1
    min_score = float('inf')

    best_motif_matrix = []

    for i in range(n - k):
        motif1 = dna[0][i:i+k]

        #for j in range(n - k):
        #    motif2 = dna[1][j:j+k]

        motif_matrix = [motif1]
        profile = buildProfile(motif_matrix, k)

        for dna_string in range(1, t):
            next_motif = profile_most_probable_kmer(dna[dna_string], k, profile)

            motif_matrix.append(next_motif)
            profile = buildProfile(motif_matrix, k)
        
        current_profile_score = score_motif_matrix(motif_matrix)

        if current_profile_score < min_score:
            
            min_score = current_profile_score
            best_motif_matrix = motif_matrix

    return best_motif_matrix


bestMotifs = greedy_motif_search(dna, k, t)

for motif in bestMotifs:
    print(motif, end= " ")

