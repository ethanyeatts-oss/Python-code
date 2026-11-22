
class DNAseq:
    def __init__(self, sequence):
        self.sequence = sequence

    def __str__(self):
        return self.sequence

    def length(self):
        return len(self.sequence)

    def reverse_strand(self):
        complement = {
            "A": "T",
            "T": "A",
            "C": "G",
            "G": "C"
        }

        return "".join(complement[base] for base in reversed(self.sequence))


dna = DNAseq("ACGATTCATTCGTCA")
print(dna.length())
print(dna.sequence)
print(dna)
print(dna.reverse_strand())
