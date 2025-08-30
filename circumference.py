import math

def calculate_circumference(radius):
  """
  Calculates the circumference of a circle given its radius.

  Args:
    radius: The radius of the circle (a float or int).

  Returns:
    The circumference of the circle (a float).
  """
  circumference = 2 * math.pi * radius
  return circumference

# Get radius input from the user
try:
  radius_input = float(input("Enter the radius of the circle: "))
  
  # Calculate and print the circumference
  circumference_result = calculate_circumference(radius_input)
  print(f"The circumference of the circle with radius {radius_input} is: {circumference_result:.2f}")

except ValueError:
  print("Invalid input. Please enter a numerical value for the radius.")

