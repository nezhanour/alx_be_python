number = int(input("Enter the size of the pattern: "))

count = 0
while count != number:
    for x in range(1, number + 1):
        print("*", end="")
    print()
    count += 1

