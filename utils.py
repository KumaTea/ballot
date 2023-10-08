import os
import json
import base64
import random
import session
from settings import temp_path


def file_path_trimmer(file_path: str, max_length: int = 16):
    r"""
    E:\Downloads\example.txt -> E:\Down...\example.txt
    file name must complete unless exceed max_length
    """
    if len(file_path) <= max_length:
        result = file_path
    else:
        file_dir, filename = os.path.split(file_path)
        if len(filename) == max_length:
            result = file_path
        elif len(filename) < max_length:
            if len('...\\' + filename) >= max_length:
                result = filename
            else:
                filename = '...\\' + filename
                more_path = file_dir[:max_length - len(filename)]
                result = more_path + filename
        else:
            result = '...' + filename[-(max_length - 3):]

    if os.name == 'nt':
        result = result.replace('/', '\\')
    return result


def choose_item(item_list=session.item_list, no_repeat=True):
    if no_repeat:
        if len(session.picked) == len(item_list):
            session.picked = []
        while True:
            item = random.choice(item_list)
            if item not in session.picked:
                # session.picked.append(item)
                break
    else:
        item = random.choice(item_list)
    return item


def write_conf(range_str, file_path, no_repeat, selected):
    with open(temp_path, 'w') as f:
        json.dump({
            'range': range_str,
            'file_path': file_path,
            'no_repeat': no_repeat,
            'selected': selected,
        }, f)


def image_to_base64(image_path):
    with open(image_path, "rb") as f:
        s = base64.b64encode(f.read())
    return s
