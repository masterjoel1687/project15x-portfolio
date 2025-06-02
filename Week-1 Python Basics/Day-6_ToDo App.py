def insertTask(task, tasks):
    tasks.append(task)
    print(f"Task '{task}' added successfully.")

def viewTasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def deleteTask(task_number, tasks):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' deleted successfully.")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            task = input("Enter the task to add: ")
            insertTask(task, tasks)
        elif choice == "2":
            viewTasks(tasks)
        elif choice == "3":
            task_number = int(input("Enter the task number to delete: "))
            deleteTask(task_number, tasks)
        elif choice == "4":
            print("Exiting the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()