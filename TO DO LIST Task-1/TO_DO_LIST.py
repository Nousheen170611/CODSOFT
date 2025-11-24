to_do_list = []

def show_menu():
    print("\n--- TO DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter the task: ")
        to_do_list.append(task)
        print("Task added!")

    elif choice == '2':
        if len(to_do_list) == 0:
            print("No tasks in the list.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(to_do_list, 1):
                print(f"{i}. {task}")

    elif choice == '3':
        if len(to_do_list) == 0:
            print("No tasks to remove.")
        else:
            print("\nSelect the task number to remove:")
            for i, task in enumerate(to_do_list, 1):
                print(f"{i}. {task}")

            try:
                remove_index = int(input("Enter number: ")) - 1
                if 0 <= remove_index < len(to_do_list):
                    removed_task = to_do_list.pop(remove_index)
                    print(f"Removed: {removed_task}")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")

    elif choice == '4':
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1–4.")
