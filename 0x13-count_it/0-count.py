#!/usr/bin/python3
"""Modulus that contains function for counting hotlist in Reddit
Functions:
    count_words: function that orders the different steps of the process
"""
import requests


def count_words(subreddit, word_list, hot_list=[], after='null'):
    """Function that orders the different steps of the process

    Args:
        subreddit (str): Topic for title of hot articles
        hot_list (list, optional): to be search. Defaults to [].
        after (None, optional): paginator. Defaults to None.

    Returns:
        list: with all titles of the topic
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    credentials = {'User-Agent': "Mozilla/5.0 (X11; CrOS x86_64 10066.0.0)\
                   AppleWebKit/537.36 (KHTML, like Gecko)\
                   Chrome/84.0.4147.105 Safari/537.36"}
    parameters = {"limit": "100", "after": after}
    response = requests.get(url,
                            headers=credentials,
                            params=parameters,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    hot_list_of_dicts = response.json().get("data").get("children")
    after = response.json().get("data").get("after")
    hot_list.extend([reddit.get("data").get("title") for
                    reddit in hot_list_of_dicts])
    if after is None:
        to_print_dict = {x: 0 for x in word_list}
        for word in word_list:
            count = 0
            for title in hot_list:
                split_title = title.split()
                new_split = [element.lower() for element in split_title]
                count = count + new_split.count(word.lower())
            if count != 0:
                to_print_dict[word] = to_print_dict[word] + count
        for elem in sorted(to_print_dict.items(), key=lambda x: (-x[1], x[0])):
            if elem[1] != 0:
                print("{}: {}".format(elem[0], elem[1]))
    else:
        return count_words(subreddit, word_list,
                           hot_list, after)
