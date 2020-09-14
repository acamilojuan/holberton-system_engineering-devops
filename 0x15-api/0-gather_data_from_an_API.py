#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}".format(
        sys.argv[1])
    res = requests.get(url)
    name = res.json().get('name')
    res = requests.get("{}/todos".format(url))
    tasks_list = res.json()
    done = []
    for task in tasks_list:
        if task.get('completed'):
            done.append(task)
    print("Employee {} is done with tasks({}/{}):".format(
        name, len(done), len(tasks_list)))
    for task_title in done:
        print("\t {}".format(task_title.get('title')))
