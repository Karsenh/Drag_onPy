import tkinter

GLOBAL_BANK_TAB_NUM = 1


def set_global_bank_tab_num(new_bank_tab_num):
    global GLOBAL_BANK_TAB_NUM
    bank_tab_num_var = new_bank_tab_num
    GLOBAL_BANK_TAB_NUM = int(bank_tab_num_var.get())
    print(f'Updated bank tab num: {GLOBAL_BANK_TAB_NUM}')
    return


def get_global_bank_tab_num():
    return GLOBAL_BANK_TAB_NUM

