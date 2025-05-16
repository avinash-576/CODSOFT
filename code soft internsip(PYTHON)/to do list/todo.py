import json

class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()
        print(f"Added: {task}")

    def list_tasks(self):
        for idx, task in enumerate(self.tasks, 1):
            status = "✔" if task["completed"] else "❌"
            print(f"{idx}. {task['task']} [{status}]")

    def mark_complete(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            self.save_tasks()
            print("Task marked as complete.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(f"Deleted: {removed_task['task']}")
        else:
            print("Invalid task number.")

def main():
    todo = ToDoList()

    while True:
        print("\nOptions: 1) Add Task 2) List Tasks 3) Complete Task 4) Delete Task 5) Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.list_tasks()
        elif choice == "3":
            num = int(input("Enter task number to complete: "))
            todo.mark_complete(num)
        elif choice == "4":
            num = int(input("Enter task number to delete: "))
            todo.delete_task(num)
        elif choice == "5":
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
    