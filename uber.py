print("Select your ride: ")
print("1. Bike")
print("2. Car")

choiceride = int(input("Enter your choice: "))

if( choiceride == 1 ): 
  print( "what type of bike? " )
  print("1.Scooty\n")
  print("2.Scooter\n")


  
  choicebike=int(input("Enter you choice2: "))
  if choicebike==1: 
    print("you have selected scooty")
    print("your ride is on your way")
  else:
    print("you have selected scooter")
    print("your ride is on your way")



elif( choiceride == 2 ): 
  print( "what type of car?" )
  print("1.Sedan")
  print("2.SUV")
  choicecar=int(input("enter your choice3: "))
  if choicecar==1:

    print("you have selected sedan")
    print("your ride is on your way")
  else:
    print("you have selected SUV")
    print("your ride is on your way")
else: 
  print("Wrong choice! Please enter 1 or 2")