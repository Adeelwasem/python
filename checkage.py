age = int(input("Enter the age: "))

if age >= 10:
    if age <= 20:
        print("The age is between 10 and 20 years old (inclusive).")
    else:
        print("The age is greater than 20 years old and is a senior.")
else:
    print("The age is less than 10 years old and is a child.")
