#!/usr/bin/python3
from collections import Counter
import operator
import requests


def count_words(subreddit, word_list, hot_list=[], after=None):
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
    hot_list = hot_list + [post.get('data', {}).get('title') for post in data.get('children', [])]
    hot = count_words(subreddit, word_list, hot_list, after)
    hot = [x.lower() for x in hot]
    word_list = [x.lower() for x in word_list]
    word_list = [(word_list)].sort()
    pre_imp = {}
    if type(word_list) is list:
        pre_imp = {k: v for k, v in zip(word_list, [0] * len(word_list))}
    cuenta = Counter(hot)
    for k, _ in pre_imp.items():
        if cuenta.get(k):
            pre_imp[k] = cuenta.get(k)
    impre = sorted(pre_imp.items(), key=operator.itemgetter(1), reverse=True)
    for i in impre:
        a, b = i
        if b > 0:
            print('{}: {}'.format(a, b))
