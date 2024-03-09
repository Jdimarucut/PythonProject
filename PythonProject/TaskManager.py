#Dimarucut,Jon Paolo
#BSCS_CS2C
#Laboratory Activity 1

import numpy as np

class TaskManager:
    def __init__(self):
        self.tasks = np.array([], dtype=str)

    def add_task(self, task):
        self.tasks = np.append(self.tasks, task)
        print(f"Added task: {task}")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks = self.tasks[self.tasks != task]
            print(f"Removed Task: {task}")
        else:
            print(f"{task} not found in the list.")

    def view_task(self):
        if self.tasks.size == 0:
            print("To-do list is empty.")
        else:
            print("To-do list:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")


task_manager = TaskManager()

while True:
    print("\nWhat do you want to do?")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. View all tasks")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter a new task: ")
        task_manager.add_task(task)
    elif choice == "2":
        task = input("Enter a task to remove: ")
        task_manager.remove_task(task)
    elif choice == "3":
        task_manager.view_task()
    elif choice == "4":
        print("Exiting")
        break
    else:
        print("Invalid Choice!")