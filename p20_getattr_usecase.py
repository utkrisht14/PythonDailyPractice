class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# Create an object
p = Person("Alice", 30)

# 1. Accessing an attribute by name
attr_name = "name"
print("Name", getattr(p, attr_name))

# 2. Accessing a method dynamically and calling it
method_name = "greet"
method = getattr(p, method_name)
print("Greeting:", method())

# 3. Providing a default value if attribute doesn't exist
print("Height", getattr(p, "height", "N/A"))

# 4. Using getattr in dynamic cases
attributes = ["name", "age", "height"]

print("\n Coming from 4th point: ")
for attr in attributes:
    value = getattr(p, attr, None)
    print(f"{attr}: {value}")

# 5. Using getattr for dynamic method execution
def execute_action(obj, action_name):
    action = getattr(obj, action_name, None)
    if callable(action):
        return action()
    return "Action not found."

print("Execute greet: ", execute_action(p, "greet"))
print("Execute height: ", execute_action(p, "height"))