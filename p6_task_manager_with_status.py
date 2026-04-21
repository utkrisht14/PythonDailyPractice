tasks = {}

def add_tasks(tasks):
    task_name = input("Enter the task name: ")
    if task_name in tasks:
        print("Task already exists.")
    else:
        tasks[task_name] = "Pending"
        print(f"{task_name} added successfully.")


def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        return

    for k, v in tasks.items():
        print(f"{k} - {v}")


def mark_complete(tasks):
    task_name = input("Enter the task name to mark as complete: ")
    if task_name in tasks:
        tasks[task_name] = "Completed"
        print(f"{task_name} marked as completed.")
    else:
        print("Task not found.")


def delete_tasks(tasks):
    task_name = input("Enter the task name to delete: ")
    if task_name in tasks:
        del tasks[task_name]
        print(f"{task_name} deleted successfully.")
    else:
        print("Task not found.")


def show_menu(tasks):
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_tasks(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_tasks(tasks)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")


# Run program
show_menu(tasks)