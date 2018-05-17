def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return bool(len(dna1) > len(dna2))


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return bool(dna2 in dna1)

def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if input sequence only contains A, T, C and G. False otherwise.

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ABCGGTC')
    False

    """
    for nucleotide in dna:
        if nucleotide not in ["A", "T", "C", "G"]:
            return False

    return True


def insert_sequence(dest, source, idx):
    """ (str, str, int) -> str

    Insert a partial sequence source into complete sequence dest at index idx.

    >>> insert_sequence('CCGG', 'AT', 2)
    CCATGG
    >>> insert_sequence('CGATAT', 'GC', 4)
    CGATGCAT
    
    """
    output = dest[:idx] + source + dest[idx:]
    return output


def get_complement(nucleotide):
    """ (str) -> str

    Return the complement of the given nucleotide.

    >>> get_complement('A')
    T
    >>> get_complement('G')
    C

    """

    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'
    else:
        return None


def get_complementary_sequence(seq):
    """ (str) -> str

    Take seq as input and return the complemet.

    >>> get_complementary_sequence('AT')
    TA
    >>> get_complementary_sequence('GC')
    CG

    """

    return seq[::-1]



