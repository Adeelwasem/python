import math

def process_number():
    """
    Prompts the user for a number, calculates its square root,
    and separates the digits of the original number into odd and even lists.
    """
    while True:
        try:
            num_str = input("Enter a positive number: ")
            number = float(num_str)
            if number < 0:
                print("Please enter a non-negative number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    # Calculate the square root
    square_root = math.sqrt(number)
    print(f"The square root of {number} is: {square_root}")

    # Separate odd and even digits
    odd_digits = []
    even_digits = []

    # Iterate through the digits of the original number (as a string)
    for digit_char in num_str:
        if digit_char.isdigit():  # Ensure it's a digit and not a decimal point
            digit = int(digit_char)
            if digit % 2 == 0:
                even_digits.append(digit)
            else:
                odd_digits.append(digit)

    print(f"Odd digits from the original number: {odd_digits}")
    print(f"Even digits from the original number: {even_digits}")

# Call the function to execute the program
process_number()