
num_values = int(input("How many values will be averaged: "))

total = 0

for i in range(1, num_values + 1):
    value = float(input("Enter value " + str(i) + ": "))
    total += value

average = total / num_values

print()
print("The average of the input values is", round(average, 2))

