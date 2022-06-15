#!/usr/bin/python3
"""gets information about user todos from an api"""
import requests
import sys


def todo_info(id):
    """prints todo info"""
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    user = requests.get(user_url).json()
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    todos = requests.get(todo_url).json()
    completed = [todo for todo in todos if todo["completed"]]
    print("Employee {} is done with tasks({}/{}):".format(
        user["name"],
        len(completed),
        len(todos)
    ))
    for todo in completed:
        print("\t {}".format(todo["title"]))


if __name__ == "__main__":
    todo_info(sys.argv[1])
