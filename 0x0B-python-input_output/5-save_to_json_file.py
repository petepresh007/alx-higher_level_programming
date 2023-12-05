#!/usr/bin/python3
"""Defines a JSON file-writing function."""


def save_to_json_file(my_obj, filename):
    """json function"""

    import json
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f, ensure_ascii=False, indent=4)
