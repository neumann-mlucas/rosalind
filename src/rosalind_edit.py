from itertools import chain, tee


def edit(data):
    _, (s, t) = zip(*gen_seqs(data))

    # M = 0 1 2 3
    #     1 0 0 0
    #     2 0 0 0
    #     3 0 0 0
    M = [
        [(i if j == 0 else (j if i == 0 else 0)) for j in range(len(t) + 1)]
        for i in range(len(s) + 1)
    ]

    def update(i, j):
        if s[i - 1] == t[j - 1]:
            return M[i - 1][j - 1]
        else:
            return min(M[i - 1][j], M[i][j - 1], M[i - 1][j - 1]) + 1

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            M[i][j] = update(i, j)

    return str(M[-1][-1])


def gen_seqs(data):
    idx_lines = (n for (n, l) in enumerate(data) if l.startswith(">"))
    # add last line to iter
    idx_lines = chain(idx_lines, (len(data),))
    for i, j in pairwise(idx_lines):
        id_seq, seq = data[i], "".join(data[i + 1 : j])
        yield id_seq, seq


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


DATA_FILE = "dat/rosalind_edit.txt"

SAMPLE_DATA = """
>Rosalind_39
PLEASANTLY
>Rosalind_11
MEANLY"""
SAMPLE_OUTPUT = "5"


if __name__ == "__main__":
    # Assert sample
    SAMPLE_DATA = SAMPLE_DATA.lstrip().split("\n")
    assert edit(SAMPLE_DATA) == SAMPLE_OUTPUT

    # Read data
    with open(DATA_FILE, "r") as f:
        data = [l.strip() for l in f.readlines()]
    # Produce output
    print(edit(data))
