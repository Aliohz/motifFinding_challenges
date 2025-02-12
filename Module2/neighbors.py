### Code Challenge: Implement Neighbors to find the d-neighborhood of a string.

### Input: A string Pattern and an integer d.
### Output: The collection of strings Neighbors(Pattern, d). (You may return the strings in any order, but each line should contain only one string.)

genome = "000000000"
d = 9

def neighbors(pattern, d):
    if d == 0:
        return {pattern}
    
    neighborhood = set()
    neighborhood.add(pattern)

    for i in range(len(pattern)):
        for nucleotide in "01":
            if nucleotide != pattern[i]:
                new_pattern = pattern[:i] + nucleotide + pattern[i+1:]
                
                for neighbor in neighbors(new_pattern, d - 1):
                    neighborhood.add(neighbor)

    return neighborhood


# Main program
neighborhood = neighbors(genome, d)

for neighbor in neighborhood:
    print(neighbor, end= " ")
#print(len(neighborhood))
