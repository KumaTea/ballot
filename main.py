from data import *
from settings import *
import PySimpleGUI as sg
from layouts import layout
from core import event_process
from starting import restore_conf


window = sg.Window(
    title=TITLE,
    icon=ICON,
    layout=layout,
    size=(400, 300),
    resizable=True,
    finalize=True
)
restore_conf(window)


if __name__ == '__main__':
    while True:
        event, values = window.read()
        print(event, values)
        event_process(window, event, values)
