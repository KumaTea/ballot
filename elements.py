from settings import *
import PySimpleGUI as sg


result_text = sg.Text(
    WELCOME,
    key='#result',
    font=("黑体", 25),
    justification='center',
)

select_range = sg.Radio(
    SEL_RANGE,
    key='#sel_range',
    group_id='choice',
    default=True,
    font=("宋体", 12),
    enable_events=True
)

range_input = sg.InputText(
    default_text='',
    key='#range',
    font=("Arial", 12),
    size=(5, 1),
    enable_events=True
)

select_file = sg.Radio(
    SEL_FILE,
    key='#sel_file',
    group_id='choice',
    font=("宋体", 12),
    enable_events=True
)

file_path_display = sg.Text(
    text=PATH_HINT,
    key='#file_path',
    font=("Consolas", 12),
    size=(16, 1),
    enable_events=True
)

file_path_invisible = sg.InputText(
    key='#file_path_invisible',
    visible=False,
    font=("Consolas", 12),
    enable_events=True
)


file_selector = sg.FileBrowse(
    target='#file_path_invisible',
    button_text=WAIT_F0R_CHOOSING,
    key='#file_selector',
    font=("Arial", 12),
    file_types=(("文本文件", "*.txt"), ("所有文件", "*.*")),
)

no_repeat_checkbox = sg.Checkbox(
    NO_REPEATING,
    key='#no_repeat',
    default=True,
    font=("宋体", 12),
    enable_events=True
)

draw_button = sg.Button(
    DRAW,
    key='#draw',
    font=("黑体", 25),
    button_color=BUTTON_COLOR_GREEN,
    border_width=2,
    size=(10, 1),
    disabled=True,
    enable_events=True
)
