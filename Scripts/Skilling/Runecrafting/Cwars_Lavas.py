from API.Interface.General import setup_interface

ROD_EQUIPPED = False
NECK_EQUIPPED = False
TIARA_EQUIPPED = False
STAFF_EQUIPPED = False


def start_crafting_lavas(curr_loop):
    if curr_loop != 1:
        print(f'Not the first loop')
    else:
        print(f'This is the first loop - setting up interface etc.')
        setup_interface("north", 1, "up")

    return True

# PSEUDO-CODE


# Start - cwars bank chest

# Check equipment - Ring of Dueling
    # ROD_EQUIPPED = True
# Check equipment - Binding Necklace
    # NECK_EQUIPPED = True
# Check equipment - Fire tiara
    # TIARA_EQUIPPED = True
# Check equipment - Mist staff
    # STAFF_EQUIPPED = True

