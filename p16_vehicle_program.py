class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}"

    def start_engine(self):
        raise NotImplementedError("Subclasses must implement this method")


class Car(Vehicle):
    def __init__(self, brand, model, seating_capacity):
        super().__init__(brand, model)
        self.seating_capacity = seating_capacity

    def start_engine(self):
        print("Car engine started with key ignition.")


class Bike(Vehicle):
    def __init__(self, brand, model, engine_capacity):
        super().__init__(brand, model)
        self.engine_capacity = engine_capacity

    def start_engine(self):
        print("Bike engine started with self-start.")


class Truck(Vehicle):
    def __init__(self, brand, model, load_capacity):
        super().__init__(brand, model)
        self.load_capacity = load_capacity

    def start_engine(self):
        print("Truck engine started with heavy ignition system.")



if __name__ == "__main__":
    v1 = Car("Toyota", "Camry", 5)
    v2 = Bike("Ducati", "Monster", 200)
    v3 = Truck("Ford", "Focus", 1000)
    print(v1.display_info())
    v2.start_engine()











