"""Parsing json, received from Twitter API"""


import json
from typing import Union


def parse_json(data: Union[list, dict]):
    """
    This function parses two types of json files - dict and list.
    """
    if not isinstance(data, list) and not isinstance(data, dict):
        print("Looks like your object is not a list or a dictionary. Here`s it:")
        print(data)
    lst = []
    if isinstance(data, dict):
        print("The object you got is a dictionary.")
        print("Select one of the keys:")
        for i in data.keys():
            lst.append(i)
        print(lst)
        key = str(input())
        while key not in lst:
            print("No such a key, try again: ", end=" ")
            key = str(input())
        data = data[key]
        while isinstance(data, dict) or isinstance(data, list):
            if isinstance(data, dict):
                print("Select one of the keys of this item: ", end=" ")
                print(data.keys())
                key = str(input())
                data = data[key]
            if isinstance(data, list):
                print(f"This list contains {len(data)} fields.")
                print("Enter a number of element you would like to display: ", end=" ")
                num = int(input())
                data = data[num-1]
        print(f'The "{key}" field value is "{data}"')

    else:
        print("The object you got is a list.")
        print(
            f"Please, enter a number (integer, from 1 to {len(data)}), to be shown:", end=" ")
        num = int(input())
        new_data = data[num-1]
        [lst.append(i) for i in data.keys()]
        print("This item contains the following keys:")
        print(lst)
        print("Enter a key to be displayed:", end=" ")
        key = str(input())
        while key not in new_data:
            print("There`s no such a key, please try again:", end=" ")
            key = str(input())
        while isinstance(new_data[key], dict) and new_data[key] != None:
            res = new_data[key]
            print("This item contains the following keys:")
            print(res.keys())
            print("Select one key from the list:", end=" ")
            key = str(input())
        if res[key] == None:
            print("Looks like this key has no value...")
        else:
            print(f'The "{key}" field value is "{res[key]}"')


def get_object(path):
    """
    This function takes a path to a .json file and returns a json object.
    """
    file = open(path, 'r', encoding='utf-8')
    data = json.load(file)
    return data


def main():
    """
    This function takes a path to a .json file and returns a json object.
    """
    print("Hi there. Please enter a path to a file with object\
 you would like to parse: ", end=" ")
    path = str(input())
    data = get_object(path)
    parse_json(data)


main()
