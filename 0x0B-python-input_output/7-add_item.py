#!/usr/bin/python3
'''A module that loads a Json file, adds to the list and then saves
the Json file'''
import sys
import json
load = __import__("6-load_from_json_file").load_from_json_file
save = __import__("5-save_to_json_file").save_to_json_file


list_obj = []

try:
    list_obj += load("add_item.json")

except FileNotFoundError:
    with open("add_item.json", 'w', encoding='utf-8') as f:
        pass

finally:
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            list_obj.append(sys.argv[i])

        save(list_obj, "add_item.json")
