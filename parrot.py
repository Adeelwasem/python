class Parrot:


    species = "bird"

    def __init__(self , name , age):
        self.name = name
        self.age = age






blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

print("Blu is a {}".format(blu.species))
print("{} is {} years old".format( woo.name,woo.age ))
