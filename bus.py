class Vehicle:
    """Represents a generic vehicle with a default fare calculation."""
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def calculate_fare(self):
        """Calculates the default fare (capacity * 100)."""
        return self.seating_capacity * 100

class Bus(Vehicle):
    """Represents a Bus that inherits from Vehicle and overrides the fare calculation."""
    def calculate_fare(self):
        
        base_fare = super().calculate_fare()
        maintenance_charge = base_fare * 0.10
        final_fare = base_fare + maintenance_charge
        return int(final_fare)


bus = Bus(50)

final_bus_fare = bus.calculate_fare()
print(f"The total fare for the bus with a seating capacity of {bus.seating_capacity} is BDT {final_bus_fare}")


generic_vehicle = Vehicle(100)
generic_fare = generic_vehicle.calculate_fare()
print(f"The total fare for a generic vehicle with a seating capacity of {generic} 50")