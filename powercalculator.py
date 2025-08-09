base = int(input("Enter the base number: "))
exponent = int(input("Enter a positive integer exponent: "))

if exponent < 0:
    print("This method only works for positive integer exponents.")
else:
    result = 1
    for _ in range(exponent):
        result *= base
    print(f"{base} raised to the power of {exponent} is: {result}")