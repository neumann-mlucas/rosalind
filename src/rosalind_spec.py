def spec(data):
    rev_table = {round(v, 2): k for (k, v) in MASS_TABLE.items()}
    deltas = (j - i for (i, j) in zip(data, data[1:]))
    return "".join([rev_table[round(d, 2)] for d in deltas])


MASS_TABLE = {
    "A": 71.03711,
    "C": 103.00919,
    "D": 115.02694,
    "E": 129.04259,
    "F": 147.06841,
    "G": 57.02146,
    "H": 137.05891,
    "I": 113.08406,
    "K": 128.09496,
    "L": 113.08406,
    "M": 131.04049,
    "N": 114.04293,
    "P": 97.052760,
    "Q": 128.05858,
    "R": 156.10111,
    "S": 87.032030,
    "T": 101.04768,
    "V": 99.068410,
    "W": 186.07931,
    "Y": 163.06333,
}


DATA_FILE = "dat/rosalind_spec.txt"

SAMPLE_DATA = """
3524.8542
3710.9335
3841.974
3970.0326
4057.0646"""
SAMPLE_OUTPUT = "WMQS"

if __name__ == "__main__":
    # Assert sample
    SAMPLE_DATA = [float(m) for m in SAMPLE_DATA.lstrip().split("\n")]
    # print(spec(SAMPLE_DATA))
    assert spec(SAMPLE_DATA) == SAMPLE_OUTPUT
    # Read data
    with open(DATA_FILE, "r") as f:
        data = [float(l) for l in f.readlines()]
    # Produce output
    print(spec(data))
