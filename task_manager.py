import os

TASK_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from file."""
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    """Save tasks to file."""
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks):
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f" Task '{task}' added successfully.")
    else:
        print("⚠ Task cannot be empty!")

def view_tasks(tasks):
    if not tasks:
        print(" No tasks found.")
    else:
        print("\n Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            choice = int(input("Enter the task number to delete: "))
            if 1 <= choice <= len(tasks):
                removed = tasks.pop(choice - 1)
                save_tasks(tasks)
                print(f"🗑 Task '{removed}' deleted successfully.")
            else:
                print("⚠ Invalid task number!")
        except ValueError:
            print("⚠ Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n==== Task Manager ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print(" Goodbye!")
            break
        else:
            print(" Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
