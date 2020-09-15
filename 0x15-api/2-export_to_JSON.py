#!/usr/bin/python3
"""Extended Python script to export data in the JSON format."""
import json
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    res = requests.get(url)
    user_name = res.json().get('username')
    res = requests.get("{}/todos".format(url))
    tasks_list = res.json()
    new_list = []
    dic_json = {}
    for task in tasks_list:
        new_dic = {}
        new_dic['task'] = task.get('title')
        new_dic['completed'] = task.get('completed')
        new_dic['username'] = user_name
        new_list.append(new_dic)
    dic_json[id] = new_list
    with open('{}.json'.format(id), 'w') as file:
        json.dump(dic_json, file)
