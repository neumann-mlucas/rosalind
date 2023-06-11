from itertools import chain, tee


def build_matrix(s, t, m, n):
    M = [[[] for x in range(n + 1)] for y in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                M[i][j] = 0
            elif s[i - 1] == t[j - 1]:
                M[i][j] = M[i - 1][j - 1] + 1
            else:
                M[i][j] = max(M[i - 1][j], M[i][j - 1])

    return M


def lcsq(data):
    s, t, *_ = [s[1] for s in gen_seqs(data)]
    i, j = len(s), len(t)
    table = build_matrix(s, t, i, j)

    seq = ""
    while i > 0 and j > 0:
        if s[i - 1] == t[j - 1]:
            seq = s[i - 1] + seq
            i -= 1
            j -= 1
        elif table[i - 1][j] > table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return seq


def gen_seqs(data):
    idx_lines = (n for (n, l) in enumerate(data) if l.startswith(">"))
    # Add last line to iter
    idx_lines = chain(idx_lines, (len(data),))
    for i, j in pairwise(idx_lines):
        id_seq, seq = data[i], "".join(data[i + 1 : j])
        yield id_seq, seq


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


DATA_FILE = "dat/rosalind_lcsq.txt"

SAMPLE_DATA = """
>Rosalind_23
AACCTTGG
>Rosalind_64
ACACTGTGA"""
SAMPLE_OUTPUT = "ACCTGG"

if __name__ == "__main__":
    # Assert sample
    SAMPLE_DATA = SAMPLE_DATA.lstrip().split("\n")
    assert lcsq(SAMPLE_DATA) == SAMPLE_OUTPUT

    # Read data
    with open(DATA_FILE, "r") as f:
        data = [l.strip() for l in f.readlines()]
    # Produce output
    print(lcsq(data))
