x = 5
if type(x) is int:
    print("true")
else:
    print("false")

x = 5.0
if type(x) is not float:
    print("true")
else:
    print("false")

x = 20
y = 20

if x is y:
    print("x & y SAME identity")

if x is not y:
    print("x & y have DIFFERENT identity")

# Changing the value of y
y = 30
