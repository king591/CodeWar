# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.
# If you want to know more http://en.wikipedia.org/wiki/DNA
# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).
# More similar exercise are found here http://rosalind.info/problems/list-view/ (source)

def DNA_strand(dna: str):
    # code here
    dna_cell = list(dna)
    for i in range(0, dna_cell.__len__()):
        if dna_cell[i] == 'T':
            dna_cell[i] = 'A'
        elif dna_cell[i] == 'A':
            dna_cell[i] = 'T'
        elif dna_cell[i] == 'C':
            dna_cell[i] = 'G'
        elif dna_cell[i] == 'G':
            dna_cell[i] = 'C'
    return ''.join(dna_cell)


def DNA_strand_1(dna: str):
    # code here
    dna_completed = ''
    for i in dna:
        if i == 'T':
            dna_completed += 'A'
        elif i == 'A':
            dna_completed += 'T'
        elif i == 'C':
            dna_completed += 'G'
        elif i == 'G':
            dna_completed += 'C'
    return dna_completed


# Best solution in python 3
def DNA_strand_2(dna: str):
    return dna.translate(str.maketrans("ATCG", "TAGC"))


dna = 'TAAGGCC'
print(DNA_strand(dna))
print(DNA_strand_1(dna))
print(DNA_strand_2(dna))
