filename = input("What is the name of the input file [default = hw18_sample_data.fasta]: ")

if filename == "":
    filename = "hw18_sample_data.fasta"

file = open(filename, "r")
sequence = ""

for line in file:
    if not line.startswith(">"):
        sequence = sequence + line.strip().upper()

file.close()

length = len(sequence)

print("\nSequence length:", length)

for letter in "ACGT":
    count = sequence.count(letter)
    percent = count / length * 100
    print(letter, "=", round(percent, 3), "%")

forward = 0
reverse = 0

for i in range(length - 2):
    if sequence[i:i+3] == "ATG":
        forward = forward + 1
    if sequence[i:i+3] == "CAT":
        reverse = reverse + 1

print("Potential start codons on forward strand:", forward)
print("Potential start codons on reverse strand:", reverse)
