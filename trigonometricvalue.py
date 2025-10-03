import math


angle_radians = math.pi / 4  
sine_value = math.sin(angle_radians)
cosine_value = math.cos(angle_radians)
tangent_value = math.tan(angle_radians)

print(f"Sine of {angle_radians} radians: {sine_value}")
print(f"Cosine of {angle_radians} radians: {cosine_value}")
print(f"Tangent of {angle_radians} radians: {tangent_value}")


angle_degrees = 30
angle_radians_from_degrees = math.radians(angle_degrees)
sine_30_degrees = math.sin(angle_radians_from_degrees)
cosine_30_degrees = math.cos(angle_radians_from_degrees)

print(f"\nSine of {angle_degrees} degrees: {sine_30_degrees}")
print(f"Cosine of {angle_degrees} degrees: {cosine_30_degrees}")



asin_value = math.asin(0.5)
print(f"\nAngle (in radians) whose sine is 0.5: {asin_value}")
print(f"Angle (in degrees) whose sine is 0.5: {math.degrees(asin_value)}")

