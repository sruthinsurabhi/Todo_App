tasks = []

def add_task():
    """Add a new task to the list"""
    name_task = input("Enter task name: ")
    tasks.append({'name': name_task, 'completed': False})
    print(f"Task '{name_task}' added to the list.")

def mark_task_completed():
    """Mark a task as completed"""
    task_name = input("Enter task name to mark as completed: ")
    for task in tasks:
        if task['name'] == task_name:
            task['completed'] = True
            print(f"Task '{task_name}' marked as completed.")
            return
    print(f"Task '{task_name}' not found in the list.")

def delete_task():
    """Delete a task from the list"""
    name_task = input("Enter task name to delete: ")
    for task in tasks:
        if task['name'] == name_task:
            tasks.remove(task)
            print(f"Task '{name_task}' deleted from the list.")
            return
    print(f"Task '{name_task}' not found in the list.")

def list_tasks():
    """List all tasks"""
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for task in tasks:
            status = 'completed' if task['completed'] else 'not completed'
            print(f"{task['name']} ({status})")

        input()
# Main loop
while True:
    print("\nTodo List App\n")
    print("1. Add task")
    print("2. Mark task as completed")
    print("3. Delete task")
    print("4. List tasks")
    print("5. Quit")

    choice = input("\nEnter your choice (1-5): ")
    if choice == '1':
        add_task()
    elif choice == '2':
        mark_task_completed()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        list_tasks()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
