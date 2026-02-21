FILE_PATH = "todos.txt"


def get_todos(filepath=FILE_PATH):
    """Return the list of todos from the file."""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath=FILE_PATH):
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_local)


if __name__ == "__main__":
    print("hello from functions")
