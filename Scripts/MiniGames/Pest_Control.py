from API.Imaging.Image import wait_for_img


SCRIPT_NAME = 'Pest_Control'


def start_pest_control(curr_loop):
    if curr_loop != 1:
        print(f'Not first loop')
        while not is_fighting():
            print(f'Searching for portal spawn to click')
            search_for_portal_spawn()

        print(f'We are supposedly fighting something...')
    else:
        print(f'First loop')
    return True


def search_for_portal_spawn():
    return wait_for_img(img_name='purple_portal', script_name=SCRIPT_NAME, threshold=0.8, should_click=True, click_middle=True, max_wait_sec=60)


def is_fighting():
    return wait_for_img(img_name='Hp', category='Exp_Drops', max_wait_sec=3)