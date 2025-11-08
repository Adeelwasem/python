class Dog:

    animal_type = "Canine"

    def __init__(self, breed, color):
        """
        Initializes a new Dog object.

        Args:
            breed (str): The breed of the dog.
            color (str): The color of the dog's coat.
        """
        self.breed = breed
        self.color = color

    def display_details(self):
        """
        Displays the details of the dog.
        """
        print(f"Animal Type: {Dog.animal_type}")
        print(f"Breed: {self.breed}")
        print(f"Color: {self.color}")
        print("-" * 20)


dog1 = Dog("Doberman", "Black and Brown")
dog2 = Dog("Labrador", "White")

print("Details of Dog 1:")
dog1.display_details()

print("Details of Dog 2:")
dog2.display_details()

