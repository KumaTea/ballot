import os


system_temp_dir = os.environ['TEMP']
temp_path = os.path.join(system_temp_dir, 'ballot.json')


# UI
TITLE = '抽签小助手 v1.0.4.7'
WELCOME = '请开始抽签'
SEL_RANGE = '从序号中抽取：'
SEL_FILE = '从文件中读取：'
PATH_HINT = '按右侧按钮'
WAIT_F0R_CHOOSING = '选择...'
NO_REPEATING = '不重复抽取'
DRAW = '抽签'
STOP = '停止'

# colors
BUTTON_COLOR_GREEN = ('white', '#00ADB5')
BUTTON_COLOR_RED = ('white', '#FF2E63')

# errors
UNKNOWN_CODEC = '无法识别文件编码！建议使用 UTF-8 保存。'
NOT_ENOUGH = '读取到的名单不足2人，请检查是否为每行1人！'
RANGE_NOT_ENOUGH = '序号范围不足2人！'
NOT_DIGIT = '序号范围必须为数字！'
FILE_NOT_FOUND = '无法读取文件。'
