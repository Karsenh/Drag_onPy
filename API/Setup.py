import time
import win32gui
from API.Debug import write_debug


# BlueStacks HWND
bsHWND = 0

# BlueStacks window x0, y0 (top-left coordinates) for offset
bsX = 0
bsY = 0
bsX2 = 0
bsY2 = 0

BS_WINDOW_HEIGHT = 877
BS_WINDOW_WIDTH = 1533


# Return the top-left coords of BlueStacks window to calculate mouseMove offset
# Invoked for every MouseMove() call
def get_bluestacks_xy():
    global bsX, bsY, bsY2, bsX2
    # hwnd = win32gui.FindWindow(None, 'Window Title')
    global bsHWND

    get_bluestacks_hwnd()
    focus_bluestacks()

    x0, y0, x1, y1 = win32gui.GetWindowRect(bsHWND)

    # write_debug(f'BlueStacks Hwnd: {bsHWND}\nTop-Left X: {x0} & Y1: {y0}\nBottom-Right X: {x1} & Y1: {y1}')

    bsX = x0
    bsY = y0
    bsX2 = x1
    bsY2 = y1
    return x0, y0


def focus_bluestacks():
    global bsHWND
    win32gui.SetForegroundWindow(bsHWND)
    # write_debug(f'Focusing BlueStacks window...')
    time.sleep(1)
    return


def get_bluestacks_window_size() -> tuple:
    global bsX, bsY, bsY2, bsX2
    w = bsX2 - bsX  # width
    h = bsY2 - bsY  # height
    # write_debug(f'Height {h} & Width: {w}')
    return w, h


def set_bluestacks_window_size(w=BS_WINDOW_WIDTH, h=BS_WINDOW_HEIGHT):
    global bsHWND

    # Get current BlueStacks window size
    global bsX
    global bsY
    global bsX2
    global bsY2

    curr_w, curr_h = get_bluestacks_window_size()

    if curr_h == BS_WINDOW_HEIGHT:
        write_debug(f'✅ BlueStacks Dimensions are correct.\n({bsX}, {bsY}, {bsX2}, {bsY2})')

    if curr_h > BS_WINDOW_HEIGHT:
        diff_h = curr_h - BS_WINDOW_HEIGHT
        diff_w = curr_w - BS_WINDOW_WIDTH
        write_debug(f'⛔ BlueStacks Dimensions are larger than required.\n({bsX}, {bsY}, {bsX2}, {bsY2})\nDifference in (curr_h - desired_h) Height = {curr_h - BS_WINDOW_HEIGHT}\nDifference in (curr_w - desired_w) Width = {curr_w - BS_WINDOW_WIDTH}')

        win32gui.MoveWindow(bsHWND, bsX, bsY, bsX2-diff_w-bsX, bsY2-diff_h-bsY, True)
        new_w, new_h = get_bluestacks_window_size()
        get_bluestacks_xy()
        write_debug(f'BlueStacks Dimensions after MoveWindow: ({bsX}, {bsY}, {bsX2}, {bsY2})\nnew_width: {new_w}, new_height: {new_h}')

    if curr_h < BS_WINDOW_HEIGHT:
        diff_h = BS_WINDOW_HEIGHT - curr_h
        diff_w = BS_WINDOW_WIDTH - curr_w
        write_debug(f'⛔ BlueStacks Dimensions are smaller than required.\n({bsX}, {bsY}, {bsX2}, {bsY2})\nDifference in (curr_h - desired_h) Height = {diff_h}\nDifference in (curr_w - desired_w) Width = {diff_w}')

        # Multiply by -1 to get absolute value
        win32gui.MoveWindow(bsHWND, bsX, bsY, bsX2+diff_w-bsX, bsY2+diff_h-bsY, True)
        new_w, new_h = get_bluestacks_window_size()
        get_bluestacks_xy()
        write_debug(f'BlueStacks Dimensions after MoveWindow: ({bsX}, {bsY}, {bsX2}, {bsY2})\n new_width: {new_w}, new_height: {new_h}')

    return


def get_bluestacks_region() -> tuple:
    # write_debug(f'Returning BlueStacks region: {bsX}, {bsY}, {bsX2}, {bsY2}')
    return bsX, bsY, bsX2, bsY2


# --- HELPERS ---


# Called in get_bluestacks_xy()
def get_bluestacks_hwnd():
    global bsHWND
    bsHWND = win32gui.FindWindow(None, 'BlueStacks App Player')
    if not bsHWND:
        print(f'⛔ERROR: BlueStacks Window Not Found! - Scripts will not start correctly. {bsHWND}')
        exit(-1)
    return


# Make x, y coords provided relative to BlueStacks window (used for mouse not screenshots)
# update_coords param added for optimization (terrible for loops)
def translate_coords(xy, update_coords=False):
    x, y = xy
    if update_coords:
        offset_x, offset_y = get_bluestacks_xy()
        return x+offset_x, y+offset_y
    else:
        offset_x, offset_y = bsX, bsY
        return x+offset_x, y+offset_y
