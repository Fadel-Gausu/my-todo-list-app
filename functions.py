todos = []

# Add Task
def add_todo():
    todo = input("Enter to-do task:\n>>> ")
    todos.append(todo)
    print(f"{todo} has been added successfully")


# View Task
def view_todo():
    if not todos:
        print("To-Do List is empty!!")
    else:
        print("To-Do List: ")
        for index, item in enumerate(todos, start=1):
            print(f"{index}. {item}")


# Edit Task
def edit_todo():
    if not todos:
        print("There are no items to update!!")
    else:
        try:
            task_num = int(input("Enter the number of the item you want to update!\n>>>"))
            new_task = input("Enter new to-do:\n>>> ")
            todos[task_num - 1] = new_task
            print(f"Task {task_num} has been updated successfully")
        except(ValueError, IndexError):
            print("Invalid task number")


# Delete Task
def delete_todo():
    if not todos:
        print("The List is empty!!")
    else:
        try:
            task_num = int(input("Enter the number of item you want to delete!\n>>>"))
            todos.pop(task_num - 1)
            print(f"{task_num} has been deleted successfully")
            print()
        except(ValueError, IndexError):
            print("Invalid task number")


# Clear Task
def clear_todo():
    if not todos:
        print("The List is empty!!")
    else:
        todos.clear()
        print("All tasks has been cleared successfully")
        print()


# Exit Task
def exit_todo():
    print("Good bye...")
    exit()
    