from tools import *
from elements import *


layout = [
    [gen_padding(10)],
    # [result_text],
    [gen_align_column([[result_text]])],
    [gen_padding(10)],
    [select_range, range_input],
    [select_file, file_path_display, file_selector, file_path_invisible],
    [gen_padding(10)],
    [gen_align_column([[no_repeat_checkbox]])],
    [gen_align_column([[draw_button]])],
]
