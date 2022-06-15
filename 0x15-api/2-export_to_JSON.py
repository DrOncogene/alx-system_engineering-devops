#!/usr/bin/python3
"""gets todo info and export it to a csv file"""
import json
import requests
import sys


def export_JSON(id):
    """exports todo to a csv"""
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    user = requests.get(user_url).json()
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    todos = requests.get(todo_url).json()
    user_name = user["username"]
    file_name = "{}.json".format(id)
    with open(file_name, "w") as f:
        user_dict = {id: []}
        for todo in todos:
            todo_dict = {}
            todo_dict["task"] = todo["title"]
            todo_dict["completed"] = todo["completed"]
            todo_dict["username"] = user_name
            user_dict[id].append(todo_dict)
        json.dump(user_dict, f)


if __name__ == "__main__":
    export_JSON(sys.argv[1])
