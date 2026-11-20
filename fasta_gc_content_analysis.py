
filename = input("What is the name of the input file [default = hw19_sample_data.fasta]: ")

if filename == "":
    filename = "hw19_sample_data.fasta"


allseq = []

with open(filename, "r") as file:
    for line in file:
        allseq.append(line)


sequences = []

for line in allseq:
    if line.startswith(">"):
        header = line.strip()
        header = header.split(" ")[0]
        parts = header.split("|")
        refnumber = parts[3]

        sequence_info = {
            "accession": refnumber,
            "sequence": ""
        }

        sequences.append(sequence_info)

    else:
        if len(sequences) > 0:
            sequences[-1]["sequence"] += line.strip()


class holddna:
    def __init__(self, accession, seq):
        self.accession = accession
        self.seq = seq

    def length(self):
        return len(self.seq)

    def gc_content(self):
        if self.length() == 0:
            return 0

        gc = self.seq.upper().count("G") + self.seq.upper().count("C")
        return (gc / self.length()) * 100


# Create holddna objects and calculate sequence information

table = []

for item in sequences:
    dna = holddna(item["accession"], item["sequence"])
    table.append(dna)


# Display results

print(f"{'Accession number':<25} {'Length':<15} {'GC content':<15}")

total_length = 0
total_gc = 0

for item in table:
    seq_length = item.length()
    gc_content = item.gc_content()

    total_length += seq_length
    total_gc += gc_content

    print(f"{item.accession:<25} {seq_length:<15} {gc_content:<15.2f}")


# Calculate averages

num_sequences = len(table)

if num_sequences > 0:
    average_length = total_length / num_sequences
    average_gc = total_gc / num_sequences
else:
    average_length = 0
    average_gc = 0


print()
print(f"Total number of sequences: {num_sequences}")
print(f"Average sequence length: {average_length:.2f}")
print(f"Average GC content: {average_gc:.2f}%")
