# from functions import get_todos, write_todos
import functions
import time

while True:
    now = time.strftime("%b %d, %Y %H:%M:%S")
    print("It is: ", now)
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:] + "\n"
        todos = functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index+1}-{item}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            todos = functions.get_todos()
            todos[number - 1] = input("New todo is: ") + "\n"
            functions.write_todos(todos)

        except ValueError:
            print("Please select a number to edit.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()

            item_to_remove = todos[number-1].strip("\n")
            print(f"Todo {number}.{item_to_remove} was removed")
            todos.pop(number-1)
            functions.write_todos(todos)

        except IndexError:
            print("That is not on the list!")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Sorry, don't understand you :-( \n")

print("Bye!")
