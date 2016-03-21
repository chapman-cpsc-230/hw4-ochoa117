"""
File: <count_pairs>
Copyright (c) 2016 <William Ochoa>
License: MIT
<This code counts the number of base pairs there are in an input strand of DNA.>
"""

def count_pair(dna, pair):
    pair = tuple(pair)
    i = 0
    for p1, p2 in zip(dna[:-1], dna[1:]):
        if (p1, p2) == pair:
            i += 1
    return i
#The code above was borrowed from Noah Waterfield Price. It counts the number of AT pairs in the DNA strand ATATGCGGACCTAT. I decided to make it general.

dna_inp = raw_input("Enter set of DNA: ")
dna = str(dna_inp)
pair_inp = raw_input("Enter a pair of bases: ")
pair = str(pair_inp)
n = count_pair(dna, pair)
print "%s appears %d times in %s" % (pair, n, dna)
