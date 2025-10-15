n = 5

for i in range(1, n+1):  # for each row
    for s in range(n - i):  # print spaces
        print(" ", end="")
    for j in range(1, i+1):  # print numbers
        print(j, end="")
    print()  # go to next line