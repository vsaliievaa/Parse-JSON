"""Parsing json, got from Twitter API"""


import json
from typing import Union


def get_object(path):
    """
    """
    file = open(path, 'r', encoding='utf-8')
    data = json.load(file)
    return data


def parse_json(data: Union[list, dict]):
    """
    """
    lst = []
    if isinstance(data, dict):
        print("The object you got is a dictionary.")
        print("Select a key from a list below:")
        for i in data.keys():
            lst.append(i)
        print(lst)
    else:
        print("The object you got is a list.")
        print(
            f"Please, enter a number (integer, from 1 to {len(data)}), to be shown:", end=" ")
        num = int(input())
        data = data[num-1]
        [lst.append(i) for i in data.keys()]
        print("This item contains the following keys:")
        print(lst)
        print("Enter a key to be displayed:", end=" ")
        key = str(input())
        while key not in data:
            print("There`s no such a key, please try again:", end=" ")
            key = str(input())
        while isinstance(data[key], dict) and data[key] != None:
            data = data[key]
            print("This item contains the following keys:")
            print(data.keys())
            print("Select one key from the list:", end=" ")
            key = str(input())
        if data[key] == None:
            print("Looks like this key has no value...")
        else:
            print(f'The "{key}" field contains this: "{data[key]}"')
