contacts = {}

def add_contact(contacts):
    name = input("Enter the name of the contact: ")
    phone_number = input("Enter the phone number: ")
    contacts[name] = phone_number
    print(f"{name} added successfully.")


def view_contacts(contacts):
    if len(contacts) == 0:
        print("No contacts found.")
        return

    for k, v in contacts.items():
        print(f"Name: {k}, Phone Number: {v}")


def search_contact(contacts):
    name = input("Enter the name to search: ")
    if name in contacts:
        print("Contact found.")
        print(f"Name: {name}, Phone Number: {contacts[name]}")
    else:
        print("Contact not found.")


def delete_contact(contacts):
    name = input("Enter the name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"{name} deleted successfully.")
    else:
        print("Contact not found.")


def show_menu():
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")


show_menu()