#!/usr/bin/python3
from collections import Counter
import operator
import requests


def hot_management(lista):
    res = [x.lower() for x in lista]
    res = ' '.join(res)
    res = res.split()
    conteo_res = Counter(res)
    return dict(conteo_res)

def impreso(inicial, reddit):
    # Vaciar valores de reddit en inicial
    # print(inicial)
    # print(reddit)
    for k in inicial.keys():
        if k in reddit:
            inicial[k] = reddit[k]
    # Ordenar inical
    d = sorted(inicial.items(), key = operator.itemgetter(1), reverse=True)
    # Impresión
    # print(d)
    for nom in d:
        a, b = nom
        if b != 0:
            print('{}: {}'.format(a, b))

def listados(lista):
    res = [x.lower() for x in lista]
    res = set(res)
    res = sorted(list(res))
    dito = {k: 0 for k in res}
    return dito

def recurse(subreddit, hot_list=[], after=None):
    '''Getting all posto of hot'''
    red_url = 'http://reddit.com/r/{}/hot.json'
    header = {'User-agent': 'Prueba:1-top_ten:v1'}
    limit = {'limit': 100}
    if isinstance(after, str):
        if after != 'STOP':
            limit['after'] = after
        else:
            return hot_list
    resp = requests.get(red_url.format(subreddit), headers=header,
                        params=limit)
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
