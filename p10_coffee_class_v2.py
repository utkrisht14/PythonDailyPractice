from typing import Optional


class Milk:
    def __init__(self, milk_amount: float, milk_temperature: float):
        self.milk_amount = milk_amount
        self.milk_temperature = milk_temperature

    def describe_milk(self):
        print(f"The milk is {self.milk_amount}ml and it is {self.milk_temperature}°C.")


class Coffee:
    def __init__(self, coffee_name: str, price: float, milk: Optional[Milk] = None):
        self.coffee_name = coffee_name
        self.price = price
        self.milk = milk

    def describe(self):
        print(f"This is a {self.coffee_name} and it costs €{self.price:.2f}.")
        if self.milk:
            self.milk.describe_milk()


class Espresso(Coffee):
    def __init__(self):
        super().__init__("Espresso", 2.50)


class Latte(Coffee):
    def __init__(self):
        milk = Milk(milk_amount=150, milk_temperature=65)
        super().__init__("Latte", 3.50, milk)


class CoffeeMachine:
    def __init__(self, machine_name: str):
        self.machine_name = machine_name

    def brew_coffee(self, coffee_type: Coffee):
        print(f"{self.machine_name} is brewing {coffee_type.coffee_name}.")
        return coffee_type


class Barista:
    def __init__(self, barista_name: str, coffee_machine: CoffeeMachine):
        self.name = barista_name
        self.coffee_machine = coffee_machine

    def make_coffee(self, coffee: Coffee):
        print(f"{self.name} is preparing your coffee.")
        brewed = self.coffee_machine.brew_coffee(coffee)
        brewed.describe()


machine = CoffeeMachine("BrewMaster Pro")
barista = Barista("Lela", machine)

espresso = Espresso()
latte = Latte()

barista.make_coffee(espresso)
print()
barista.make_coffee(latte)