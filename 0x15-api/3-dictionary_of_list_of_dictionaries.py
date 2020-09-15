#!/usr/bin/python3
"""Extended Python script to export data in the JSON format."""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    res = requests.get(url)
    dic_json = {}
    for user_id in range(1, len(res.json()) + 1):
        dic_json[user_id] = []
        req_user = requests.get("{}/{}".format(url, user_id))
        user_name = req_user.json().get('username')
        task_req = requests.get("{}/{}/todos".format(url, user_id))
        task_list = task_req.json()
        new_list = []
        for task in task_list:
            new_dic = {}
            new_dic['task'] = task.get('title')
            new_dic['completed'] = task.get('completed')
            new_dic['username'] = user_name
            new_list.append(new_dic)
        dic_json[user_id] = new_list
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dic_json, file)
