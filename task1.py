import json



# Initialize an empty task list

tasks = []



def add_task(task_name, priority, due_date):

    # Create a new task and append it to the task list

    task = {

        'name': task_name,

        'priority': priority,

        'due_date': due_date,

        'completed': False

    }

    tasks.append(task)

    save_tasks()



def remove_task(task_index):

    # Remove a task at a specific index

    if 0 <= task_index < len(tasks):

        del tasks[task_index]

        save_tasks()



def mark_completed(task_index):

    # Mark a task as completed

    if 0 <= task_index < len(tasks):

        tasks[task_index]['completed'] = True

        save_tasks()



def list_tasks():

    # Display tasks in a list with details

    for i, task in enumerate(tasks):

        print(f'{i + 1}. {task["name"]} (Priority: {task["priority"]}, Due Date: {task["due_date"]}, Completed: {task["completed"]})')



def save_tasks():

    # Save tasks to a file (e.g., tasks.json)

    with open('tasks.json', 'w') as file:

        json.dump(tasks, file)



def load_tasks():

    # Load tasks from a file (e.g., tasks.json)

    try:

        with open('tasks.json', 'r') as file:

            global tasks

            tasks = json.load(file)

    except FileNotFoundError:

        tasks = []



# You can implement a simple command-line interface for user interaction



# Load existing tasks from the file (if any)

load_tasks()



while True:

    # Display a menu for users to interact with the to-do list

    print("To-Do List Menu:")

    print("1. Add Task")

    print("2. Remove Task")

    print("3. Mark Task as Completed")

    print("4. List Tasks")

    print("5. Exit")

    choice = input("Enter your choice: ")



    if choice == "1":

        task_name = input("Task Name: ")

        priority = input("Priority (High/Medium/Low): ")

        due_date = input("Due Date (YYYY-MM-DD): ")

        add_task(task_name, priority, due_date)



    elif choice == "2":

        task_index = int(input("Enter the task index to remove: "))

        remove_task(task_index - 1)



    elif choice == "3":

        task_index = int(input("Enter the task index to mark as completed: "))

        mark_completed(task_index - 1)



    elif choice == "4":

        list_tasks()



    elif choice == "5":

        save_tasks()

        break
