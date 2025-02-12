# Solve the Pattern Matching Problem. All starting positions in Genome where Pattern appears as a substring.

file = open(r"C:\Users\Abn3r\Documents\PythonProjects\Bioinformatics\Module1\Vibrio_cholerae.txt", "r")
genome = file.read()
pattern = "CTTGATCAT"
n = len(genome) + 1
k = len(pattern)

startingPositions = []

for i in range(0, n - k):
    seq = ""
    
    for j in range(0, k):
        seq += genome[i + j]
    
    if seq == pattern:
        startingPositions.append(i)

if len(startingPositions) > 0:
    output = open("v_cholerae_startingpos.txt", "x")

for i in range(len(startingPositions)):
    position = startingPositions[i]
    output.write(str(position) + " ")

output.close()
file.close()