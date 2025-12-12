class Ferrari:
    def fuel_type(self):
        print("Fuel Type: Petrol")

    def max_speed(self):
        print("Max Speed: 350 Km/h")

class BMW:
    def fuel_type(self):
        print("Fuel Type: Diesel")

    def max_speed(self):
        print("Max Speed: 240 Km/h")


def car_details(obj):
    obj.fuel_type()
    obj.max_speed()


ferrari_obj = Ferrari()
bmw_obj = BMW()


print("Ferrari details:")
car_details(ferrari_obj)

print("\nBMW details:")
car_details(bmw_obj)