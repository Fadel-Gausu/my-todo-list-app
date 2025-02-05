    # 01/22/2024
# TO-DO APPLICATION
# ===================

# Features of the TO-DO List APP
# 1. ADD a Task
# 2. DELETE a task
# 3. EDIT a Task
# 4. VIEW a Task

print()
print("     ====================================")
print("     =   WELCOME TO MY TO-DO LIST APP   =")
print("     ====================================")
print()

todos = []
while True:
    option = input("CHOOSE AN OPTION BELOW: \n1. ADD \n2. VIEW \n3. EDIT \n4. DELETE \n5. CLEAR \n6. EXIT\n\n>>> ")

    if option == "1":
        # Add Task
        todo = input("Enter to-do task:\n>>> ")
        todos.append(todo)
        print(f"{todo} has been added successfully")
        print()
    elif option == "2":
        if not todos:
            print("To-Do List is empty!!")
        else:
            print("To-Do List: ")
            for index, item in enumerate(todos, start=1):
                print(f"{index}. {item}")
            print()

    elif option == "3":
        if not todos:
            print("There are no items to update!!")
        else:
            try:
                task_num = int(input("Enter the number of the item you want to update!\n>>>"))
                new_task = input("Enter new to-do:\n>>> ")
                todos[task_num - 1] = new_task
                print(f"Task {task_num} has been updated successfully")
                print()
            except(ValueError, IndexError):
                print("Invalid task number")

    elif option == "4":
        if not todos:
            print("The List is empty!!")
        else:
            try:
                task_num = int(input("Enter the number of item you want to delete!\n>>>"))
                todos.pop(task_num - 1)
                print(f"{todo} has been deleted successfully")
                print()
            except(ValueError, IndexError):
                print("Invalid task number")

    elif option == "5":
        if not todos:
            print("The List is empty!!")
        else:
            todos.clear()
            print("All tasks has been cleared successfully")
            print()

    elif option == "6":
        print("Good bye...")
        exit()
    else:
        pass