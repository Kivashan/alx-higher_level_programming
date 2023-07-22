#!/usr/bin/python3
'''A module that loads a Json file, adds to the list and then saves
the Json file'''
import sys
import json
load = __import__("6-load_from_json_file").load_from_json_file
save = __import__("5-save_to_json_file").save_to_json_file


try:
    list_obj = load("add_item.json")

except FileNotFoundError:
    list_obj = []

finally:
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            list_obj.append(sys.argv[i])

        save(list_obj, "add_item.json")
