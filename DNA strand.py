'''
In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G".
You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side.
DNA strand is never empty or there is no DNA at all (again, except for Haskell).
'''


def DNA_strand(dna):
    dna_reverse = ''
    for s in dna:
        if s.lower() == 'a':
            dna_reverse += 'T'
        elif s.lower() == 't':
            dna_reverse += 'A'
        elif s.lower() == 'c':
            dna_reverse += 'G'
        elif s.lower() == 'g':
            dna_reverse += 'C'
    return dna_reverse

    # return "".join([{'A':'T', 'T':'A', 'C':'G', 'G':'C'}[l] for l in dna]) однострочный вариант

print(DNA_strand("atgcgcg"))


