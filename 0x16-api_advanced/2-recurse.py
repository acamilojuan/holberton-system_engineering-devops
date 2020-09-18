#!/usr/bin/python3
"""Recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], data_after=''):
    """Fx to make the query and return list with titles of all articles"""
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                 data_after)
    headers_dict = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'}
    res = requests.get(url, headers=headers_dict, allow_redirects=False)
    if res.status_code == 200:
        data_after = res.json().get('data').get('after')
        data_children = res.json().get('data').get('children')
        for elem in data_children:
            hot_list.append(elem.get('data').get('title'))
        if data_after is None:
            return hot_list
        return recurse(subreddit, hot_list, data_after)
    else:
        return None
