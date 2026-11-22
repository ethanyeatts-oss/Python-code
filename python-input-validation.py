while True:
    x = input("Enter a number (blank to stop): ")

    if x == "":
        break

    try:
        int(x)
        print("Valid number")
    except:
        print("Not a valid number")
