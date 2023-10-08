import os
import json
from settings import temp_path
from core import selected_file


def read_conf():
    if os.path.exists(temp_path):
        with open(temp_path, 'r') as f:
            return json.load(f)
    else:
        return {}


def restore_conf(window):
    try:
        conf = read_conf()
        if conf:
            window['#range'].update(value=conf['range'])
            window['#file_path_invisible'].update(value=conf['file_path'])
            selected_file(window, file_path=conf['file_path'], passive=True)
            window['#no_repeat'].update(value=conf['no_repeat'])
            if conf['selected'] == 'range':
                window['#sel_range'].update(value=True)
                window['#sel_file'].update(value=False)
            else:
                window['#sel_range'].update(value=False)
                window['#sel_file'].update(value=True)
            window['#draw'].update(disabled=False)
            return window
    except Exception:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return window
