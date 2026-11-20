
filename = input("What is the name of the input file [default = hw18_sample_data.fasta]: ")

if filename == "":
    filename = "hw18_sample_data.fasta"

seq = ""


def get_kmer(seq):
    kmer_list = []

    ksize = int(input("size of k-mers? "))

    topn = int(input("top n of k-mers? "))

    if topn <= 0:
        print("Invalid top n value.")
        return

    if ksize <= 0 or ksize > len(seq):
        print("Invalid k-mer size.")
        return

    kamount = len(seq) - ksize + 1

    for i in range(len(seq) - ksize + 1):
        kmer = seq[i:i + ksize]
        kmer_list.append(kmer)

    freq_kmers = {}

    for kmer in kmer_list:
        if kmer in freq_kmers:
            freq_kmers[kmer] += 1
        else:
            freq_kmers[kmer] = 1

    unique_kmers = len(freq_kmers)

    unique_max = 4 ** ksize

    print()
    print(f"Total number of k-mers: {kamount}")
    print(f"Unique k-mers found: {unique_kmers}")
    print(f"Maximum possible unique k-mers: {unique_max}")
    print()

    sorted_kmers = sorted(
        freq_kmers.items(),
        key=lambda x: x[1],
        reverse=True
    )

    print(f"Top {topn} most frequent k-mers:")
    print()

    for kmer, count in sorted_kmers[:topn]:
        print(f"K-mer: {kmer}")
        print(f"Count: {count}")

    a_freq = seq.count("A") / len(seq)
    c_freq = seq.count("C") / len(seq)
    g_freq = seq.count("G") / len(seq)
    t_freq = seq.count("T") / len(seq)

    nucleotide_freq = {
        "A": a_freq,
        "C": c_freq,
        "G": g_freq,
        "T": t_freq
    }

    print()
    print("Expected counts:")

    for kmer, count in sorted_kmers[:topn]:

        probability = 1

        for nucleotide in kmer:
            probability = probability * nucleotide_freq[nucleotide]

        expected = probability * kamount

        print(f"K-mer: {kmer}")
        print(f"Observed count: {count}")
        print(f"Expected count: {expected:.1f}")
        print()


with open(filename, "r") as file:
    for line in file:
        if not line.startswith(">"):
            seq += line.strip()


seq = seq.upper()

a_count = seq.count("A")
c_count = seq.count("C")
g_count = seq.count("G")
t_count = seq.count("T")

length = len(seq)

print(f"Length of sequence: {length:,}")
print()

a_freq = seq.count("A") / len(seq)
c_freq = seq.count("C") / len(seq)
g_freq = seq.count("G") / len(seq)
t_freq = seq.count("T") / len(seq)

print("Observed nucleotide frequencies")
print(f"A = {a_freq:.3f}")
print(f"C = {c_freq:.3f}")
print(f"G = {g_freq:.3f}")
print(f"T = {t_freq:.3f}")
print()

get_kmer(seq)

startcodon = "ATG"

count = 0

for i in range(len(seq) - 2):
    if seq[i:i + 3] == startcodon:
        count = count + 1

print(f"Potential start codons on forward strand: {count}")
print()

count2 = 0
Rstartcodon = "CAT"

for i in range(len(seq) - 2):
    if seq[i:i + 3] == Rstartcodon:
        count2 = count2 + 1

print(f"Potential start codons on reverse strand: {count2}")
