from math import factorial


def lia(k, N):
    p = 1 - sum([prob(n, k) for n in range(N)])
    return f"{p:.3f}"


def prob(n, k):
    return binomial(2**k, n) * 0.25**n * 0.75 ** (2**k - n)


def binomial(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


DATA_FILE = "dat/rosalind_lia.txt"

SAMPLE_DATA = "2 1"
SAMPLE_OUTPUT = "0.684"

if __name__ == "__main__":
    # Assert sample
    SAMPLE_DATA = map(int, SAMPLE_DATA.split(" "))
    assert lia(*SAMPLE_DATA) == SAMPLE_OUTPUT
    # Read data
    with open(DATA_FILE, "r") as f:
        k, n = map(int, f.readline().strip().split(" "))
    # Produce output
    print(lia(k, n))
