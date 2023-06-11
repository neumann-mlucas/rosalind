def kpm(seq):
    failure_array = [0] * len(seq)

    for i in range(1, len(seq)):
        j = failure_array[i - 1]
        while j > 0 and seq[i] != seq[j]:
            j = failure_array[j - 1]
        if seq[i] == seq[j]:
            j += 1
        failure_array[i] = j

    return " ".join(map(str, failure_array))


DATA_FILE = "dat/rosalind_kmp.txt"

SAMPLE_DATA = """
>Rosalind_87
CAGCATGGTATCACAGCAGAG"""
SAMPLE_OUTPUT = "0 0 0 1 2 0 0 0 0 0 0 1 2 1 2 3 4 5 3 0 0"

if __name__ == "__main__":
    # Assert sample
    SAMPLE_DATA = SAMPLE_DATA.split("\n")[-1]
    assert kpm(SAMPLE_DATA) == SAMPLE_OUTPUT
    # Read data
    with open(DATA_FILE, "r") as f:
        seq = "".join(l.strip() for l in f.readlines() if not l.startswith(">"))
    # Produce output
    print(kpm(seq))
