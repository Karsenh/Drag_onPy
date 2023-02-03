import json
import jwt


class ScriptAccess:
    def __init__(self, btn_state):
        self.state = btn_state


kourend_crab_killer_btn_state = ScriptAccess('disabled')
barb_fisher_btn_state = ScriptAccess('disabled')
red_chin_btn_state = ScriptAccess('disabled')

all_scripts = [kourend_crab_killer_btn_state, red_chin_btn_state]


def set_script_access(user_licenses):
    print(f"set_script_access 🔥'ed - user_licenses: {user_licenses}")

    for lic in user_licenses:
        print(f'Decoding License and setting Script Access for license: {lic}')

        try:
            decoded_lic = jwt.decode(lic, "your-256-bit-secret", algorithms=["HS256"])
            print(f'decoded_lic: {decoded_lic}')
            update_script_state(decoded_lic)
        except:
            print(f'decoded token is invalid - likely expired. Remove from user doc.')
            return False

    # license_obj = json.load(license)

    print(f'kourend_crab_killer: {kourend_crab_killer_btn_state.state}')
    return True


def update_script_state(decoded_lic):
    enabled = 'enabled'
    disabled = 'disabled'

    if decoded_lic['category'] == 'all_access':
        print(f'👑 - All Access Granted')
        for script in all_scripts:
            script.state = 'enabled'
    elif decoded_lic['category'] == 'package':
        print(f'📦 - Package Access')
    elif decoded_lic['category'] == 'individual':
        print(f'📃 - Individual Script')
        match(decoded_lic['name']):
            case 'kourend_crab_killer':
                kourend_crab_killer_btn_state.state = enabled
            case 'barb_fisher':
                barb_fisher_btn_state.state = enabled
            case 'red_chin_hunter':
                red_chin_btn_state.state = enabled
    return
