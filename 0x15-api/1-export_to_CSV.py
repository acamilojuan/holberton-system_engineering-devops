#!/usr/bin/python3
"""Extended Python script to export data in the CSV format."""
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    res = requests.get(url)
    user_name = res.json().get('username')
    res = requests.get("{}/todos".format(url))
    tasks_list = res.json()
    with open('{}.csv'.format(user_id), 'w') as file:
        for elem in tasks_list:
            file.write('"{}","{}","{}","{}"\n'
                       .format(user_id, user_name, elem.get('completed'),
                               elem.get('title')))
