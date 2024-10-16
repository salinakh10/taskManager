import json
import os

# Dummy login credentials (Email and Password)
DUMMY_EMAIL = "testuser@example.com"
DUMMY_PASSWORD = "password123"


# Class to represent a Task
class Task:
    #  using constructor method (__init__)
    def __init__(self, id, title, completed=False): #default value = "False"
        self.id = id #stores the id parameter in the object’s id attribute
        self.title = title
        self.completed = completed

    def __repr__(self): #defines how to represent the task as a string when you print it
        return f"ID: {self.id} | Title: {self.title} | Completed: {'Yes' if self.completed else 'No'}" #using f-string formatting to insert values
    

# List to store tasks
tasks = [] #empty list


# Function to handle user login
def login():
    """Handle user login."""
    print("Login to access the Task Manager CLI")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if email == DUMMY_EMAIL and password == DUMMY_PASSWORD:
        print("Login successful!\n")
        return True  # Successful login
    else:
        print("Invalid email or password. Try again.\n")
        return False  # Failed login
    

# Function to add a new task
def add_task(title):
    '''Add a new task to the list.'''
    task_id = len(tasks) + 1  # The ID will be the next number
    new_task = Task(task_id, title) #Task constructor taking two parameters
    tasks.append(new_task)
    print(f"Task '{title}' added successfully!")

# Function to view all tasks
def view_tasks():
    '''View all tasks.'''
    if not tasks:
        print("No tasks available.")
    else:
        for task in tasks:
            print(task)

# Function to delete a task by ID
def delete_task(task_id):
    """Delete a task by its ID."""
    global tasks
    new_tasks = []  # Create an empty list to hold tasks that we want to keep
    # Loop through each task and only add the ones we want to keep
    for task in tasks:
        if task.id != task_id:  # If the task's ID is not the one we're deleting
            new_tasks.append(task)  # Add it to the new list

    tasks = new_tasks  # Update the original tasks list with the new one
    print(f"Task with ID {task_id} has been deleted.")

# Function to mark a task as complete
def mark_task_complete(task_id):
    """Mark a task as completed by its ID."""
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            print(f"Task {task_id} marked as completed.")
            return
    print(f"Task with ID {task_id} not found.")


# Function to save tasks to a JSON file
def save_tasks():
    """Save the list of tasks to a JSON file."""
    with open('tasks.json', 'w') as file:
        # Creates an empty list to hold the task dictionaries
        task_list = []
        for task in tasks:
            task_list.append(task.__dict__)  # Add each task's dictionary representation 
        # Write the list of task dictionaries to the file
        json.dump(task_list, file)
    print("Tasks saved to tasks.json")

# Function to load tasks from a JSON file
def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            task_dicts = json.load(file)
            global tasks
            tasks = [Task(task['id'], task['title'], task['completed']) for task in task_dicts]
        print("Tasks loaded from tasks.json")
    else:
        print("No saved tasks found.")

# Function to display the menu
def display_menu():
    """Display the main menu for the task manager."""
    print("\nTask Manager CLI")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task Complete")
    print("5. Save Tasks")
    print("6. Load Tasks")
    print("7. Exit")

# Main function to run the command-line interface
def run_cli():
     # First, attempt login
    if not login():  # If login fails, stop execution
        return
    

    load_tasks()  # Load tasks at the start
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':  # Add Task
            title = input("Enter task title: ")
            add_task(title)

        elif choice == '2':  # View Tasks
            view_tasks()

        elif choice == '3':  # Delete Task
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)

        elif choice == '4':  # Mark Task Complete
            task_id = int(input("Enter task ID to mark as complete: "))
            mark_task_complete(task_id)

        elif choice == '5':  # Save Tasks
            save_tasks()

        elif choice == '6':  # Load Tasks
            load_tasks()

        elif choice == '7':  # Exit
            save_tasks()  # Save tasks before exiting
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Entry point of the script
if __name__ == "__main__":
    run_cli()

