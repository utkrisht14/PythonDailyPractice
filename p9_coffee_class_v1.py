class Coffee:
    def __init__(self, name: str = "Generic Coffee", temperature: int = 0):
        self.name = name
        self.temperature = temperature

    def describe(self):
        print(f"This is a {self.name} and served at {self.temperature} degrees.")


class Espresso(Coffee):
    def __init__(self):
        super().__init__("Espresso", 100)


class Latte(Coffee):
    def __init__(self):
        super().__init__("Latte", 200)


class CoffeeMachine:
    def __init__(self, machine_name: str):
        self.machine_name = machine_name

    def brew_coffe(self, coffee_type: Coffee) -> Coffee:
        print(f"{self.machine_name} is brewing {coffee_type.name}...")
        return coffee_type

class Barista:
    def __init__(self, name:str, coffee_machine:CoffeeMachine):
        self.name = name
        self.coffee_machine = coffee_machine

    def make_coffee(self, coffee:Coffee):
        print(f"{self.name} is preparing your coffee.")
        brewed = self.coffee_machine.brew_coffe(coffee)
        brewed.describe()

# Use
my_espresso = Espresso()
my_latte = Latte()
my_coffee_machine = CoffeeMachine("My Coffee Machine")
my_barista = Barista("Lela", my_coffee_machine)

my_barista.make_coffee(my_espresso)
print()
my_barista.make_coffee(my_latte)
