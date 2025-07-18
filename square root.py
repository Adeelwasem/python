"""WAP to enter a no and display to hex and octal equivalent and its square root"""

import math

# enter a number
num = int(input("Enter a number: "))
# convvert
hex_num = hex(num)
oct_num = oct(num)

# convert
sqrt_num = math.sqrt(num)

print("Hexadecimal equivalent:", hex_num)
print("Octal equivalent:", oct_num)
print("Square root:", sqrt_num)