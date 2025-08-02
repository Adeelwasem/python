medical_cause=input("did you have a medical cause YES or NO: ")
atten = int(input("enter the attendance of the student: "))



if medical_cause == 'Yes' or medical_cause == 'yes':
    print("You are allowed")
else:
    if atten>=75:
        print("Allowed")
    else:
        print("Not allowed")


