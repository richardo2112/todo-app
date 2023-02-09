FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ opens a file and reads it into a list
        of todo items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ writes a list into a file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print(__name__)
    print(get_todos())