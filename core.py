import sys
from tools import *
from settings import *
import PySimpleGUI as sg
from lists import get_list_from_file, get_list_from_range
from utils import file_path_trimmer, choose_item, write_conf


def filled_range(window):
    # auto select range
    if not window['#sel_range'].get():
        window['#sel_range'].update(value=True)
    window['#draw'].update(disabled=False)
    return


def selected_file(window, values=None, file_path=None, passive=False):
    if not file_path:
        file_path = values['#file_path_invisible']
    # auto select file
    if not passive and not window['#sel_file'].get():
        window['#sel_file'].update(value=True)
    # display file
    window['#file_path'].update(value=file_path_trimmer(file_path))
    # enable draw button
    if not passive:
        window['#draw'].update(disabled=False)
    return


def event_process(window, event, values):
    if event == sg.WIN_CLOSED:
        window.close()
        return sys.exit(0)
    elif event == '#range':  # filled range
        return filled_range(window)
    elif event == '#file_path_invisible':  # selected file
        return selected_file(window, values)
    elif event == '#draw':
        if session.status == 'drawing':
            session.status = ''
            # change button
            window['#draw'].update(
                DRAW,
                button_color=BUTTON_COLOR_GREEN,
            )
            # stop shuffle
            # not session.flush_thread.stop()
            session.flushing = False
            # wait until thread ends
            session.flush_thread.join()
            session.flush_thread = None
            # generate result
            result = choose_item(session.item_list, values['#no_repeat'])
            session.picked.append(result)
            # update result
            window['#result'].update(value=result)
            # enable other buttons
            window['#range'].update(disabled=False)
            window['#file_selector'].update(disabled=False)
            return
        else:
            # check file
            if window['#sel_range'].get():  # range
                item_list, error = get_list_from_range(values['#range'])
                if error:
                    # inform
                    gen_error_window(error)
                    # reset range
                    window['#range'].update(value='')
                    window['#draw'].update(disabled=True)
                    return
                else:
                    session.item_list = item_list
            else:
                item_list, error = get_list_from_file(values['#file_path_invisible'])
                if error:
                    # inform
                    gen_error_window(error)
                    # clear file path
                    window['#file_path'].update(value=PATH_HINT)
                    window['#file_path_invisible'].update(value='')
                    window['#draw'].update(disabled=True)
                    return
                else:
                    session.item_list = item_list

            # passed check
            session.status = 'drawing'
            # change button
            window['#draw'].update(
                STOP,
                button_color=BUTTON_COLOR_RED
            )
            # disable other buttons
            window['#range'].update(disabled=True)
            window['#file_selector'].update(disabled=True)
            # start drawing
            start_flush_thread(window['#result'], session.item_list)
            # write config to temp file
            write_conf(
                values['#range'],
                values['#file_path_invisible'],
                values['#no_repeat'],
                'range' if window['#sel_range'].get() else 'file'
            )
            return
