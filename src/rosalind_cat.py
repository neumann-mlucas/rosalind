# Apparently Catalan numbers are not useful here!
# from: https://github.com/cdeterman/Rosalind
def cat(seq):
    # if sequence not in dictionary
    if seq not in cache:
        # iterate over range by 2's as we don't want odd lengths
        tmp = []
        for k in range(1, len(seq), 2):
            """Multiply first half of the string * the first nt and ending nt
            of first half * second half This multiplication is to combine the
            number of noncrossing perfect matches from the subproblems. The
            actual value/counts comes from the dynamically generated
            dictionary."""
            tmp.append(cat(seq[1:k]) * cache[seq[0] + seq[k]] * cat(seq[k + 1 :]))
        # assign current sequence into dictionary for later use
        cache[seq] = sum(tmp)
    return cache[seq]


cache = {
    "": 1,
    "A": 0,
    "C": 0,
    "G": 0,
    "U": 0,
    "AA": 0,
    "AC": 0,
    "AG": 0,
    "AU": 1,
    "CA": 0,
    "CC": 0,
    "CG": 1,
    "CU": 0,
    "GA": 0,
    "GC": 1,
    "GG": 0,
    "GU": 0,
    "UA": 1,
    "UC": 0,
    "UG": 0,
    "UU": 0,
}

DATA_FILE = "dat/rosalind_cat.txt"

SAMPLE_DATA = """
>Rosalind_57
AUAU"""
SAMPLE_OUTPUT = "2"

if __name__ == "__main__":
    # Assert sample
    SAMPLE_DATA = SAMPLE_DATA.lstrip().split("\n")[-1]
    assert str(cat(SAMPLE_DATA)) == SAMPLE_OUTPUT

    # Read data
    with open(DATA_FILE, "r") as f:
        seq = "".join(l.strip() for l in f.readlines() if not l.startswith(">"))
    # Produce output
    print(cat(seq))
