# 1A Compute the Number of Occurrences of a Pattern in a Text

text = "TACGCATTACAAAGCACA"
pattern = "AA"

def PatternCount(text, pattern):
    count = 0

    for i in range(0, len(text) - len(pattern)):
        
        seq = ""

        for j in range(0, len(pattern)):
            seq += text[i+j]

        if seq == pattern:
            count += 1

    return count

result = PatternCount(text, pattern)
print(result)
