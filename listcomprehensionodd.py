def get_odd_numbers_under_input():
    """
    Prompts the user for a number and returns a list of all odd numbers 
    strictly less than the input number.
    """
    while True:
        try:
            user_input = int(input("Enter a positive integer: "))
            if user_input <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    
    odd_numbers = [num for num in range(1, user_input) if num % 2 != 0]
    return odd_numbers


odd_numbers_list = get_odd_numbers_under_input()
print(f"The odd numbers less than your input are: {odd_numbers_list}")



fruits = ["apple", "banana", "cherry", "date","orange","watermelon","strawberry"]

 
if fruits:  
     
    fruits[0] = fruits[0][0].upper() + fruits[0][1:]

 
updated_fruits = fruits 


print(updated_fruits) 
