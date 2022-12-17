import os


proj_root_path = os.getcwd()

ROOT_SCREENSHOTS_PATH = f'{proj_root_path}\Assets\Screenshots'
ROOT_COMPARATORS_PATH = f'{ROOT_SCREENSHOTS_PATH}\Comparators'

AUTH_SCREEN_PATH = f'{ROOT_COMPARATORS_PATH}\Auth'
BANKING_SCREEN_PATH = f'{ROOT_COMPARATORS_PATH}\Banking'
GENERAL_SCREEN_PATH = f'{ROOT_COMPARATORS_PATH}\General'
SCRIPTS_SCREEN_PATH = f'{ROOT_COMPARATORS_PATH}\Scripts'

BS_SCREEN_PATH = f'{proj_root_path}\Assets\Screenshots\BlueStacks_ScreenShot.png'
CUSTOM_IMG_PATH = f'{proj_root_path}\{ROOT_SCREENSHOTS_PATH}\Comparators\Custom'


# LOGGING
STOP_LOG_PATH = f'{proj_root_path}\Logs\Stop_Log.txt'
DEBUG_PATH = f'{proj_root_path}\Logs\Debug_Log.txt'