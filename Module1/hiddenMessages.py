# What is the most frequent 3-mer of CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA?


nucleotides = ["A", "T", "C", "G"]
genome = "CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA"
k = 3

# All possible 3-mers (64)
kmers = []

for nucleotide1 in nucleotides:
    for nucleotide2 in nucleotides:
        for nucleotide3 in nucleotides:
            seq = nucleotide1 + nucleotide2 + nucleotide3
            kmers.append(seq)

# All possible 3-mers in genome
genome_kmers = []

for i in range(0, len(genome)-2):
    seq = genome[i] + genome[i+1] + genome[i+2]
    genome_kmers.append(seq)

# Counting
for kmer in kmers:
    ocurrence = genome_kmers.count(kmer)
    if ocurrence > 1:
        print(kmer, end= " ")
        print(ocurrence)