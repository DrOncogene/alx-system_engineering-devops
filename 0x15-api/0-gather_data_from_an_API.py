#!/usr/bin/python3
"""gets information about user todos from an api"""
import requests
import sys


def todo_info(user_id: int):
    """prints todo info"""
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user = requests.get(user_url).json()
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)
    todos = requests.get(todo_url).json()
    completed_todos = [todo for todo in todos if todo.get("completed")]
    print("Employee {} is done with tasks({}/{})".format(
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
    todo_info(sys.argv[1])
