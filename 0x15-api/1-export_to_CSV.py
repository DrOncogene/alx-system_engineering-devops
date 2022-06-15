#!/usr/bin/python3
"""gets todo info and export it to a csv file"""
import csv
import requests
import sys


def export_todo(id):
    """exports todo to a csv"""
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    user = requests.get(user_url).json()
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    todos = requests.get(todo_url).json()
    user_name = user["name"]
    file_name = "{}.csv".format(id)
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        for todo in todos:
            row = [id, user_name]
            row.append(todo["completed"])
            row.append(todo["title"])
            writer.writerow(row)


if __name__ == "__main__":
    export_todo(sys.argv[1])
