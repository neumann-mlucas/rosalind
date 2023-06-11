from itertools import chain, product
from collections import Counter


def conv(data):
    convolution = [
        round(i, 5) for i in chain(*((i - j, j - i) for (i, j) in product(*data)))
    ]
    largest_mult = Counter(convolution).most_common()[0]
    return "\n".join(map(str, reversed(largest_mult)))


DATA_FILE = "dat/rosalind_conv.txt"

SAMPLE_DATA = """
186.07931 287.12699 548.20532 580.18077 681.22845 706.27446 782.27613 968.35544 968.35544
101.04768 158.06914 202.09536 318.09979 419.14747 463.17369"""
SAMPLE_OUTPUT = """
3
85.03163"""


if __name__ == "__main__":
    # Assert sample
    SAMPLE_DATA = [
        [float(i) for i in l.split()] for l in SAMPLE_DATA.lstrip().split("\n")
    ]
    assert str(conv(SAMPLE_DATA)) == SAMPLE_OUTPUT[1:]

    # Read data
    with open(DATA_FILE, "r") as f:
        data = [[float(i) for i in l.strip().split()] for l in f.readlines()]
    # Produce output
    print(conv(data))
