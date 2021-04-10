num_sel = int(input("Select a number beetween 1 an 100: "))

x = range(num_sel)

for n in x:

    if (n + 1) % 3 == 0:
        print("fizz")

    elif (n + 1) % 5 == 0:
        print("buzz")

    else:
        print(n + 1)

