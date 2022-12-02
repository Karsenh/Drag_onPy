import subprocess
import os


def get_hwid():
    hwid = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
    return hwid

# print(f'Get id: {get_hwid()}')