print("FIZZBUZZ")

num_sel = int(input("Select a number beetween 1 an 100: "))

for n in range(1 , num_sel + 1):

    if n % 3 == 0 and n % 5 == 0:
        print("fizzbuzz")

    elif n % 3 == 0:
        print("fizz")

    elif n % 5 == 0:
        print("buzz")

    else:
        print(n)