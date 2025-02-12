def profile_most_probable_kmer(text, k, profile):

    nucleotides = {'A', 'C', 'G', 'T'}

    max_probability = -1.0

    most_probable_kmer = ""

 

    for i in range(len(text) - k + 1):

        kmer = text[i:i+k]

        probability = 1.0

 

        for j, nucleotide in enumerate(kmer):

            probability *= profile[nucleotide][j]

 

        if probability > max_probability:

            max_probability = probability

            most_probable_kmer = kmer

 

    return most_probable_kmer

 

def form_profile(motifs):

    k = len(motifs[0])

    profile = {nucleotide: [0] * k for nucleotide in 'ACGT'}

    t = len(motifs)

 

    for i in range(k):

        column = [motif[i] for motif in motifs]

        for nucleotide in 'ACGT':

            count = column.count(nucleotide)

            profile[nucleotide][i] = count / t

 

    return profile

 

def score_motifs(motifs):

    k = len(motifs[0])

    t = len(motifs)

    score = 0

 

    for i in range(k):

        column = [motif[i] for motif in motifs]

        max_count = max(column.count(nucleotide) for nucleotide in 'ACGT')

        score += t - max_count

 

    return score

 

def greedy_motif_search(dna, k, t):

    best_motifs = [seq[:k] for seq in dna]

    for i in range(len(dna[0]) - k + 1):

        motif1 = dna[0][i:i+k]

        motifs = [motif1]

 

        for j in range(1, t):

            profile = form_profile(motifs)

            most_probable_kmer = profile_most_probable_kmer(dna[j], k, profile)

            motifs.append(most_probable_kmer)
            print(motifs)

 

        if score_motifs(motifs) < score_motifs(best_motifs):
            print(score_motifs(motifs))
            best_motifs = motifs

    return best_motifs

 

Dna = '''
GACCTACGGTTACAACGCAGCAACCGAAGAATATTGGCAA
TCATTATCGATAACGATTCGCCGGAGGCCATTGCCGCACA
GGAGTCTGGTGAAGTGTGGGTTATGGGGCAGACTGGGAAA
GAATCCGATAACTGACACCTGCTCTGGCACCGCTCTCATC
AAGCGCGTAGGCGCGGCTTGGCATCTCGGTGTGTGGCCAA
AATTGAAAGGCGCATCTTACTCTTTTCGCTTAAAATCAAA
GGTATAGCCAGAAAGCGTAGTTAATTTCGGCTCCTGCCAA
TCTGTTGTTGCTAACACCGTTAAAGGCGGCGACGGCAACT
'''
Dna = Dna.split()
k = 5
t = 8


best_motifs = greedy_motif_search(Dna, k, t)

for motif in best_motifs:

    print(motif)