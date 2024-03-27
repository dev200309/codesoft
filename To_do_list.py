import os

# Function to display the main menu
def display_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    print("============================")

# Function to view the to-do list
def view_tasks():
    if not os.path.exists("tasks.txt"):
        print("To-Do list is empty.")
        return

    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    if not tasks:
        print("To-Do list is empty.")
    else:
        print("\n===== TO-DO LIST =====")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task.strip()}")
        print("=======================")

# Function to add a new task to the to-do list
def add_task():
    task = input("Enter task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully!")

# Function to mark a task as completed
def mark_completed():
    view_tasks()
    task_num = int(input("Enter task number to mark as completed: "))
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    
    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1] = tasks[task_num - 1].replace(" [ ] ", " [x] ")
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task():
    view_tasks()
    task_num = int(input("Enter task number to delete: "))
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    
    if 1 <= task_num <= len(tasks):
        del tasks[task_num - 1]
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

# Main function to run the application
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
