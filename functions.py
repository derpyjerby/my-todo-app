# We added a constant FILEPATH so that if ever we decide to change the name of the file, we can just update "FILEPATH"
# This can also be seen when we run dir(functions)
FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
        Read a text file and returns the list of to-do items.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
