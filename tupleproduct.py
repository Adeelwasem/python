from functools import reduce
import operator


tuple1 = (4, 3, 2, 2, -1, 18)
tuple2 = (2, 4, 8, 8, 3, 2, 9)


product1 = reduce(operator.mul, tuple1)


product2 = reduce(operator.mul, tuple2)


print(f"The product of all numbers in tuple1 is: {product1}")
print(f"The product of all numbers in tuple2 is: {product2}")


combined_tuple = tuple1 + tuple2
print(f"Concatenated tuple: {combined_tuple}")


repeated_tuple = tuple1 * 2
print(f"Tuple1 repeated twice: {repeated_tuple}")


print(f"First element of tuple1: {tuple1[0]}")
print(f"Last element of tuple2: {tuple2[-1]}")

