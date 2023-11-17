import os
import json
from datetime import datetime

class Task:
    def __init__(self, description, priority="medium", due_date=None, completed=False):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.description} | Priority: {self.priority} | Due Date: {self.due_date} | Status: {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def mark_task_completed(self, task):
        task.completed = True

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def save_to_file(self, filename="tasks.json"):
        with open(filename, "w") as file:
import os
import json
from datetime import datetime

class Task:
    def __init__(self, description, priority="medium", due_date=None, completed=False):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.description} | Priority: {self.priority} | Due Date: {self.due_date} | Status: {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def mark_task_completed(self, task):
        task.completed = True

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def save_to_file(self, filename="tasks.json"):
        with open(filename, "w") as file:
            tasks_data = [{"description": task.description,
                           "priority": task.priority,
                           "due_date": task.due_date,
                           "completed": task.completed}
                          for task in self.tasks]
            json.dump(tasks_data, file, indent=2)

    def load_from_file(self, filename="tasks.json"):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                tasks_data = json.load(file)
                self.tasks = [Task(task["description"],
                                   task["priority"],
                                   task["due_date"],
                                   task["completed"])
                              for task in tasks_data]

def main():
    todo_list = ToDoList()

    # Load tasks from file if available
    todo_list.load_from_file()

    while True:
        print("\n==== To-Do List ====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Save and Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter task priority (high/medium/low): ")
            due_date_str = input("Enter due date (YYYY-MM-DD): ")
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d") if due_date_str else None

            new_task = Task(description, priority, due_date)
            todo_list.add_task(new_task)
            print("Task added successfully!")

        elif choice == "2":
            todo_list.display_tasks()
            task_index = int(input("Enter the task number to remove: ")) - 1

            try:
                task_to_remove = todo_list.tasks[task_index]
                todo_list.remove_task(task_to_remove)
                print("Task removed successfully!")
            except IndexError:
                print("Invalid task number.")

        elif choice == "3":
            todo_list.display_tasks()
            task_index = int(input("Enter the task number to mark as completed: ")) - 1

            try:
                task_to_complete = todo_list.tasks[task_index]
                todo_list.mark_task_completed(task_to_complete)
                print("Task marked as completed!")
            except IndexError:
                print("Invalid task number.")

        elif choice == "4":
            todo_list.display_tasks()

        elif choice == "5":
            todo_list.save_to_file()
            print("Tasks saved. Exiting.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
￼Enter            tasks_data = [{"description": task.description,
                           "priority": task.priority,
                           "due_date": task.due_date,
                           "completed": task.completed}
                          for task in self.tasks]
            json.dump(tasks_data, file, indent=2)

    def load_from_file(self, filename="tasks.json"):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                tasks_data = json.load(file)
                self.tasks = [Task(task["description"],
                                   task["priority"],
                                   task["due_date"],
                                   task["completed"])
                              for task in tasks_data]

def main():
    todo_list = ToDoList()

    # Load tasks from file if available
    todo_list.load_from_file()

    while True:
        print("\n==== To-Do List ====")
        print("1. Add Task")
  print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Save and Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter task priority (high/medium/low): ")
            due_date_str = input("Enter due date (YYYY-MM-DD): ")
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d") if due_date_str else None

            new_task = Task(description, priority, due_date)
            todo_list.add_task(new_task)
            print("Task added successfully!")

        elif choice == "2":
            todo_list.display_tasks()
            task_index = int(input("Enter the task number to remove: ")) - 1

            try:
                task_to_remove = todo_list.tasks[task_index]
                todo_list.remove_task(task_to_remove)
                print("Task removed successfully!")
            except IndexError:
