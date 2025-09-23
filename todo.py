def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Remove task")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            if not tasks:
                print("No tasks yet!")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif choice == "2":
            new_task = input("Enter task: ")
            tasks.append(new_task)
            save_tasks(tasks)
            print(f"✅ Task '{new_task}' added.")

        elif choice == "3":
            if not tasks:
                print("No tasks available to update.")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                try:
                    task_no = int(input("Enter task number to update: "))
                    if 0 < task_no <= len(tasks):
                        new_text = input("Enter new task text: ")
                        old_task = tasks[task_no-1]
                        tasks[task_no-1] = new_text
                        save_tasks(tasks)
                        print(f"🔄 Task '{old_task}' updated to '{new_text}'.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            if not tasks:
                print("No tasks available to remove.")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                try:
                    task_no = int(input("Enter task number to remove: "))
                    if 0 < task_no <= len(tasks):
                        removed = tasks.pop(task_no-1)
                        save_tasks(tasks)
                        print(f"❌ Task '{removed}' removed.")
                    else:
                        print("Invalid number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "5":
            print("👋 Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
