import json

tasks = []

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

def add_task():
    title = input("Enter task title: ")
    task = {"title": title, "completed": False}
    tasks.append(task)
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks):
        status = "✓" if task["completed"] else "✗"
        print(f"{index+1}. {task['title']} [{status}]")
        
def mark_complete():
    view_tasks()
    num = int(input("Enter task number: "))

    if 0 < num <= len(tasks):
        tasks[num-1]["completed"] = True
        print("Marked complete!")
    else:
        print("Invalid number.")


def delete_task():
    view_tasks()
    num = int(input("Enter task number: "))

    if 0 < num <= len(tasks):
        tasks.pop(num-1)
        print("Task deleted!")
    else:
        print("Invalid number.")



def show_menu():
    print("\n--- Student Task Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Save and Exit")
    
    
    
load_tasks()


while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        mark_complete()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        save_tasks()
        print("Tasks saved. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")

