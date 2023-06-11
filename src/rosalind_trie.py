def trie(seqs):
    # Reset Class
    Node.mark_overall = 0
    Node.answer = []

    root = Node()
    for seq in seqs:
        root.append(seq)
    return "\n".join(Node.answer[1:])


class Node:
    # keep a count of the number of nodes
    mark_overall = 0
    # store tree repr
    answer = []

    def __init__(self, codon="", parent=1):
        Node.mark_overall += 1
        # Those 3 attr identify the node
        self.parent = parent
        self.mark = Node.mark_overall
        self.codon = codon
        # This is the final output
        Node.answer.append(str(self))

    def __repr__(self):
        return f"{self.parent} {self.mark} {self.codon}"

    def append(self, string):
        head, *tail = string
        if len(string) == 1:
            setattr(self, head, Node(head, self.mark))
        elif hasattr(self, head):
            getattr(self, head).append(tail)
        else:
            # needs to be in 2 lines 'cos setattr returns None
            setattr(self, head, Node(head, self.mark))
            getattr(self, head).append(tail)


DATA_FILE = "dat/rosalind_trie.txt"

SAMPLE_DATA = """
ATAGA
ATC
GAT"""
SAMPLE_OUTPUT = """
1 2 A
2 3 T
3 4 A
4 5 G
5 6 A
3 7 C
1 8 G
8 9 A
9 10 T"""

if __name__ == "__main__":
    # Assert sample
    SAMPLE_DATA = SAMPLE_DATA.lstrip().split("\n")
    assert trie(SAMPLE_DATA) == SAMPLE_OUTPUT.lstrip()
    # Read data
    with open(DATA_FILE, "r") as f:
        data = [l.strip() for l in f.readlines()]
    # Produce output
    print(trie(data))
