#!/usr/bin/python3
"""Function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """Fx to make the query and print the 10 1st hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers_dict = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'}
    res = requests.get(url, headers=headers_dict, allow_redirects=False)
    if res.status_code == 200:
        resp = res.json().get('data').get('children')
        for elem in range(10):
            print(resp[elem].get('data').get('title'))
    else:
        print('None')
