def swap_variables(a, b, c, d):
    print("Before swap: a =", a, "b =", b, "c =", c, "d =", d)
    a, b, c, d = d, c, b, a
    print("After swap: a =", a, "b =", b, "c =", c, "d =", d)

# Example usage
swap_variables(5, 10, 20, 30)
