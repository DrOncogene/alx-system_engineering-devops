#!/usr/bin/python3
"""exports all users' todo info to a json file"""
import json
import requests


def export_all_to_JSON():
    """exports todo to a json for all users"""
    users_url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(users_url).json()
    file_name = "todo_all_employees.json"
    all_users_todos = {}
    for user in users:
        uid = user["id"]
        url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(uid)
        todos = requests.get(url).json()
        user_todo_list = []
        for todo in todos:
            todo_dict = {}
            todo_dict["username"] = user["username"]
            todo_dict["task"] = todo["title"]
            todo_dict["completed"] = todo["completed"]
            user_todo_list.append(todo_dict)
        all_users_todos[uid] = user_todo_list

    with open(file_name, "w") as f:
        json.dump(all_users_todos, f)


if __name__ == "__main__":
    export_all_to_JSON()
