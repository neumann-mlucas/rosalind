from math import factorial


def mmch(seq):
    a, u, g, c = map(seq.count, ["A", "U", "G", "C"])

    a = factorial(max(a, u)) // factorial(max(a, u) - min(a, u))
    b = factorial(max(g, c)) // factorial(max(g, c) - min(g, c))

    return "%i" % (a * b)


DATA_FILE = "dat/rosalind_mmch.txt"

SAMPLE_DATA = """
>Rosalind_57
AUGCUUC"""
SAMPLE_OUTPUT = "6"

if __name__ == "__main__":
    # Assert sample
    SAMPLE_DATA = SAMPLE_DATA.lstrip().split("\n")[-1]
    print(mmch(SAMPLE_DATA))
    # assert mmch(SAMPLE_DATA) == SAMPLE_OUTPUT

    # Read data
    with open(DATA_FILE, "r") as f:
        seq = "".join(l.strip() for l in f.readlines() if not l.startswith(">"))
    # Produce output
    print(mmch(seq))
