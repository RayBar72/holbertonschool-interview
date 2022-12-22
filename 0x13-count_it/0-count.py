#!/usr/bin/python3
"""Modulus that contains function for counting hotlist in Reddit
Functions:
    hot_management: takes a list an counts the number of times that
                    a word happens
    impreso: prints the results
    listados: converts into a dictionary the list of words to be searched
    recurse: searches the hotlis topics. Recursive function
    count_words: function that orders the different steps of the process
"""
import requests


def impreso(inicial, reddit):
    """Function that prints the occurrence of searched words

    Args:
        inicial (list): to be searched
        reddit (list): to search
    """
    count = {}
    for word in inicial:
        count[word] = 0
    for title in reddit:
        for word in inicial:
            for title_word in title.lower().split():
                if title_word == word.lower():
                    count[word] += 1
    count = {k: v for k, v in count.items() if v > 0}
    words = list(count.keys())
    for word in sorted(words,
                       reverse=True, key=lambda k: count[k]):
        print("{}: {}".format(word, count[word]))


def count_words(subreddit, word_list, hot_list=[], after=None):
    """Function that orders the different steps of the process

    Args:
        subreddit (str): Topic for title of hot articles
        hot_list (list, optional): to be search. Defaults to [].
        after (None, optional): paginator. Defaults to None.

    Returns:
        list: with all titles of the topic
    """
    red_url = 'http://reddit.com/r/{}/hot.json'
    headers = {'User-agent': 'Unix:elrayi:v1'}
    limit = {'limit': 100}
    if isinstance(after, str):
        if after != "STOP":
            limit['after'] = after
        else:
            return impreso(word_list, hot_list)
    response = requests.get(red_url.format(subreddit),
                            headers=headers, params=limit)
    if response.status_code != 200:
        return None
    data = response.json().get('data', {})
    after = data.get('after', 'STOP')
    if not after:
        after = "STOP"
    hot_list = hot_list + [post.get('data', {}).get('title')
                           for post in data.get('children', [])]
    return count_words(subreddit, word_list, hot_list, after)
