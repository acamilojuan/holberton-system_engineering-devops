#!/usr/bin/python3
"""Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If an invalid
subreddit is given, the function should return 0."""
import requests


def number_of_subscribers(subreddit):
    """Fx to return the number of suscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers_dict = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'}
    res = requests.get(url, headers=headers_dict, allow_redirects=False)
    subscribers = res.json().get('data').get('subscribers')
    return subscribers
