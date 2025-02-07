    # 01/22/2024
# TO-DO APPLICATION
# ===================

# Features of the TO-DO List APP
# 1. ADD a Task
# 2. DELETE a task
# 3. EDIT a Task
# 4. VIEW a Task

from functions import *

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
        add_todo()
    elif option == "2":
        view_todo()

    elif option == "3":
        edit_todo()

    elif option == "4":
        delete_todo()

    elif option == "5":
        clear_todo()

    elif option == "6":
        exit_todo()
    else:
        pass

# 2/7/2025
# a module is a file of reusable code.
# 3 types are:
# 1. Built-in
# 2. Third party
# 3. Custom module
# they can be used by importing them
# syntax:
#   import [module name]