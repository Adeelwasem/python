def print_mirrored_right_angle_triangle(height):
    for i in range(1, height + 1):
        # Print leading spaces
        for j in range(height - i):
            print(" ", end="")
        # Print stars
        for k in range(i):
            print("^", end="")
        print( )
        
height = int(input("Enter the height of the triangle: "))
print_mirrored_right_angle_triangle(height)
