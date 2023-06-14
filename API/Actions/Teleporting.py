from API.Imaging.Image import does_img_exist, get_existing_img_xy, wait_for_img
from API.Interface.General import is_tab_open
from API.Mouse import mouse_long_click, mouse_click


CACHED_INVENT_CRAFTING_CAPE_XY = None


def teleport_with_crafting_cape(is_equipped=False):
    global CACHED_INVENT_CRAFTING_CAPE_XY
    print(f'Teleporting with Crafting Cape...')

    # Open the tab which the crafting cape is in (equipment or inventory)
    if not is_equipped:
        if not is_tab_open(tab='inventory'):
            print(f'⛔ Failed to open inventory in teleport_crafting_cape method in API > Actions > Teleporting')
            return False
    else:
        if not is_tab_open('equipment'):
            print(f'Failed to open equipment tab in teleport_crafting_cape method in API > Actions > Teleporting')
            return False

    if CACHED_INVENT_CRAFTING_CAPE_XY:
        mouse_long_click(CACHED_INVENT_CRAFTING_CAPE_XY)
    # Get the cape coordinates
    else:
        if not does_img_exist(img_name='crafting_cape', category='Teleports', img_sel='inventory', threshold=0.85):
            print(f'⛔ Failed to find Crafting Cape in inventory in API > Actions > Teleporting')
            return False
        cape_x, cape_y = get_existing_img_xy()
        adj_xy = cape_x + 10, cape_y + 10

        CACHED_INVENT_CRAFTING_CAPE_XY = adj_xy

        # Long click for options
        mouse_long_click(adj_xy)

    # Select teleport option
    if not does_img_exist(img_name='crafting_cape_teleport_option', category='Teleports', should_click=True, click_middle=True):
        print(f'⛔ Failed to find Crafting Cape Teleport option in API > Actions > Teleporting')
        return False

    return wait_for_img(img_name='crafting_guild_flag', category='Teleports')


def teleport_with_spellbook(location):
    if not is_tab_open('magic'):
        print(f'⛔ Failed to open Magic tab in API > Actions > Teleporting method lunar_teleport')
        return False

    if not does_img_exist(img_name=f'{location}_teleport_spell', category='Teleports', should_click=True, click_middle=True):
        print(f'⛔ Failed to find {location}_teleport_spell')
        return False

    return wait_for_img(img_name='Magic', category='Exp_Drops', threshold=0.7)