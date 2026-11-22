
total = 0
count = 0

while True:
    value = input("Enter a value (leave blank to finish): ")

    if value == "":
        break

    total += float(value)
    count += 1

average = total / count

print()
print("The average of the input values is", round(average, 2))
