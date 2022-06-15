#!/usr/bin/python3
"""gets information about user todos from an api"""
import requests
import sys


def todo_info(user_id: int):
    """prints todo info"""
    user_res = requests.get("https://jsonplaceholder.typicode.com/users/{:s}"
                            .format(user_id))
    user = user_res.json()
    todo = requests.get("https://jsonplaceholder.typicode.com/users/{:s}/todos"
                        .format(user_id))
    todos = todo.json()
    completed_todos = [todo for todo in todos if todo.get("completed")]
    print("Employee {:s} is done with tasks({}/{})".format(
        user.get("name"),
        len(completed_todos),
        len(todos)
    ))
    for todo in completed_todos:
        print("\t {:s}".format(todo.get("title")))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No employee ID passed")
        sys.exit(1)
    user_id = sys.argv[1]
    todo_info(user_id)
