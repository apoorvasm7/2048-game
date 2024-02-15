
import json
from datetime import datetime

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name, priority="medium", due_date=None):
        task = {"name": task_name, "priority": priority, "due_date": due_date, "completed": False}
        self.tasks.append(task)
        print(f"Task '{task_name}' added.")

    def remove_task(self, task_name):
        for task in self.tasks:
            if task["name"] == task_name:
                self.tasks.remove(task)
                print(f"Task '{task_name}' removed.")
                return
        print(f"Task '{task_name}' not found in the list.")

    def mark_completed(self, task_name):
        for task in self.tasks:
            if task["name"] == task_name:
                task["completed"] = True
                print(f"Task '{task_name}' marked as completed.")
                return
        print(f"Task '{task_name}' not found in the list.")

    def show_tasks(self):
        if self.tasks:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task['name']} - Priority: {task['priority']}, Due Date: {task['due_date']}, Completed: {task['completed']}")
        else:
            print("No tasks in the list.")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.tasks, file)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            pass

def main():
    todo_list = TodoList()
    todo_list.load_from_file("tasks.json")
    
    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Mark task as completed")
        print("4. Show tasks")
        print("5. Save tasks to file")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task_name = input("Enter the task name: ")
            priority = input("Enter the priority (high/medium/low): ")
            due_date = input("Enter the due date (YYYY-MM-DD) (optional): ")
            if due_date:
                due_date = datetime.strptime(due_date, "%Y-%m-%d")
            todo_list.add_task(task_name, priority, due_date)
        elif choice == '2':
            task_name = input("Enter the task name to remove: ")
            todo_list.remove_task(task_name)
        elif choice == '3':
            task_name = input("Enter the task name to mark as completed: ")
            todo_list.mark_completed(task_name)
        elif choice == '4':
            todo_list.show_tasks()
        elif choice == '5':
            todo_list.save_to_file("tasks.json")
            print("Tasks saved to file.")
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()