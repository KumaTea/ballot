# UI TOOLS


# import base64
import session
from data import *
from time import sleep
import PySimpleGUI as sg
from random import shuffle
from threading import Thread


def gen_padding(size):
    return sg.Text(
        " ",
        size=(1, 1),
        font=("Arial", size),
    )


def gen_align_column(elements, align='center'):
    return sg.Column(
        elements,
        justification=align,
    )


def gen_error_window(msg, title='错误'):
    # with open('icons/red-error.png', "rb") as f:
    #     s = base64.b64encode(f.read())
    return sg.popup_ok(
        msg,
        icon=RED_ERROR_ICON,
        image=ORANGE_ERROR_ICON,
        title=title,
    )


def text_flush(textbox, item_list, delay=1/24):
    shuffled_list = item_list.copy()
    shuffle(shuffled_list)
    while True:
        for item in shuffled_list:
            if session.flushing:
                textbox.update(value=item)
                sleep(delay)
            else:
                return None


def start_flush_thread(textbox, item_list, delay=1/24):
    session.flushing = True
    session.flush_thread = Thread(target=text_flush, args=(textbox, item_list, delay))
    session.flush_thread.start()
