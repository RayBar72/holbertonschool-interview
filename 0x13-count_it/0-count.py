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
from collections import Counter
import operator
import requests


def hot_management(lista):
    """Function that takes a list an counts the number of times of occurence

    Args:
        lista (list): list returned of recurse

    Returns:
        dictionary with all the occurrence of each word in the list
    """
    res = [x.lower() for x in lista]
    res = ' '.join(res)
    res = res.split()
    conteo_res = Counter(res)
    return dict(conteo_res)


def impreso(inicial, reddit):
    """Function that prints the occurrence of searched words

    Args:
        inicial (list): to be searched
        reddit (list): to search
    """
    for k in inicial.keys():
        if k.lower() in reddit:
            inicial[k] = reddit[k.lower()]
    d = sorted(inicial.items(), key=operator.itemgetter(1), reverse=True)
    for nom in d:
        a, b = nom
        if b != 0:
            print('{}: {}'.format(a, b))


def listados(lista):
    """Function that converts into a dictionary the list of words to be
       searched

    Args:
        lista (list): words to be searched

    Returns:
        dict: dictionary in zero with the words to be searched
    """
    # res = [x.lower() for x in lista]
    # res = set(res)
    res = sorted(list(lista))
    dito = {k: 0 for k in res}
    return dito


def recurse(subreddit, hot_list=[], after=None):
    """Function that orders the different steps of the process

    Args:
        subreddit (str): Topic for title of hot articles
        hot_list (list, optional): to be search. Defaults to [].
        after (None, optional): paginator. Defaults to None.

    Returns:
        list: with all titles of the topic
    """
    red_url = 'http://reddit.com/r/{}/hot.json'
    header = {'User-agent': 'Prueba:1-top_ten:v1'}
    limit = {'limit': 100}
    if isinstance(after, str):
        if after != 'STOP':
            limit['after'] = after
        else:
            return hot_list
    resp = requests.get(red_url.format(subreddit),
                        headers=header,
                        params=limit)
    uno = resp.status_code
    if resp.status_code != 200:
        return None
    data = resp.json().get('data', {})
    after = data.get('after', 'STOP')
    if not after:
        after = 'STOP'
    hot_list = hot_list + [post.get('data', {}).get('title')
                           for post in data.get('children', [])]
    return recurse(subreddit, hot_list, after)


def count_words(subreddit, word_list):
    hots_lists = recurse(subreddit)
    if hots_lists:
        initial = listados(word_list)
        hot_dict = hot_management(hots_lists)
        impreso(initial, hot_dict)
    else:
        return None
