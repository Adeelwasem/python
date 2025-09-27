try:
    age_str = input("Please enter your age: ")
    age = int(age_str)

    if age < 0:
        
        raise ValueError("Age cannot be negative.")

    if age % 2 == 0:
        print(f"Your age, {age}, is an even number.")
    else:
        print(f"Your age, {age}, is an odd number.")
except ValueError as ex:
    print(f"The Exception is: {ex}. Please enter a valid whole number for your age.")