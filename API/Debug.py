import sys
from datetime import datetime
from API.Imports.Paths import DEBUG_PATH
import inspect


DEBUG_MODE = True
MEM_USAGE_OBJS = []


def get_is_debug():
    global DEBUG_MODE
    return DEBUG_MODE


def set_is_debug(new_val):
    global DEBUG_MODE
    is_debug = new_val.get()
    print(f'is_global_debug: {is_debug}')
    DEBUG_MODE = is_debug
    return


def log_to_debug(text):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(
        f'\n🧪 DEBUG @ [{current_time}]: - {text}'
        f'Logging to Debug_Log.txt')

    with open(f'{DEBUG_PATH}', 'a') as f:
        f.write(f'\nDEBUG @ {current_time}: {text}')

    return


def clear_debug_log():
    with open(f'{DEBUG_PATH}', 'r+') as file:
        file.truncate(0)
    return


def write_debug(text, to_file=False):
    if DEBUG_MODE:
        print(f'\n🐛 DEBUG - {inspect.currentframe().f_back.f_code.co_name} executed:\n{text}\n')
        if to_file:
            print(f'📝 to Debug_Log')
            log_to_debug(text)
    return


def add_mem_obj(obj_name, obj_val):
    global MEM_USAGE_OBJS
    new_obj = {
        'name': obj_name,
        'value': obj_val
    }
    MEM_USAGE_OBJS.append(new_obj)
    print(f'Successfully appended new obj to MEM_USAGE_OBJS: {new_obj}')
    return


def clear_mem_objs():
    global MEM_USAGE_OBJS
    MEM_USAGE_OBJS = []
    print(f'✅ Successfully cleared MEM_USAGE_OBJS: (curr val) {MEM_USAGE_OBJS}')
    return


def print_mem_objs():
    print(f'#### 🧠 MEMORY PROFILE 🧠 ####')
    for obj in MEM_USAGE_OBJS:
        print(f'{obj.name} : {sys.getsizeof(obj.value)}')
    print(f'###############################')
    return
