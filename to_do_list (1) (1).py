def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")


tasks = []

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append({"task": task, "completed": False})
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, start=1):
                status = "✔ Completed" if t["completed"] else "❌ Pending"
                print(f"{i}. {t['task']} - {status}")

    elif choice == "3":
        task_no = int(input("Enter task number to mark as completed: "))
        if 1 <= task_no <= len(tasks):
            tasks[task_no - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    elif choice == "4":
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(tasks):
            deleted = tasks.pop(task_no - 1)
            print(f"Deleted task: {deleted['task']}")
        else:
            print("Invalid task number.")

    elif choice == "5":
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")