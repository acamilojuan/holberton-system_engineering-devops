#!/usr/bin/python3
"""Extended Python script to export data in the JSON format."""
import requests
import sys
import json


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    res = requests.get(url)
    user_name = res.json().get('username')
    res = requests.get("{}/todos".format(url))
    tasks_list = res.json()
    new_list = []
    dic_json = {}
    for elem in tasks_list:
        new_dic = {}
        new_dic['elem'] = elem.get('title')
        new_dic['completed'] = elem.get('completed')
        new_dic['username'] = user_name
        new_list.append(new_dic)
    dic_json[user_id] = new_list
    with open('{}.json'.format(user_id), 'w') as file:
        json.dump(dic_json, file)
