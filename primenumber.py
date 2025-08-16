lower = int(input("Enter a lower range: "))
upper = int(input("Enter a upper range: "))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(1, 98):
  
   if num > 1:
       for i in range(2, 4):
           if (num % i) == 0:
               break
       else:
           print(num)