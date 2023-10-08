from settings import *


ch_enc = [
    # sorted by frequency
    'utf-8',
    'gbk',
    'gb2312',
    'gb18030',
    'big5',
]


def try_read_file(file: str):
    for enc in ch_enc:
        try:
            with open(file, 'r', encoding=enc) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
    raise UnicodeError(UNKNOWN_CODEC)


def get_list_from_file(file: str):
    item_list = []
    error = None

    try:
        content = try_read_file(file)
        item_list = content.split('\n')
        item_list = [item.strip() for item in item_list if item.strip()]
        if len(item_list) <= 1:
            error = NOT_ENOUGH
        return item_list, error
    except UnicodeError as e:
        error = str(e)
    except FileNotFoundError:
        error = FILE_NOT_FOUND
    return item_list, error


def get_list_from_range(num: str):
    if not num.isdigit():
        return [], NOT_DIGIT
    num = int(num)
    if num <= 1:
        return [], RANGE_NOT_ENOUGH
    return [str(i) for i in range(1, num + 1)], None
