import jwt


class ScriptAccess:
    def __init__(self, btn_state):
        self.btn_state = btn_state


initial_state = 'disabled'

kourend_crab_killer_script = cow_killer_script = pisc_iron_script = \
    barb_fisher_script = red_chin_script = motherlode_mine_script = \
    blast_furance_script = black_lizards_script = dhide_bodies_script = \
    tithe_farmer_script \
    = ScriptAccess(initial_state)

all_scripts = [kourend_crab_killer_script, cow_killer_script, pisc_iron_script, barb_fisher_script, red_chin_script,
               motherlode_mine_script, blast_furance_script, dhide_bodies_script, tithe_farmer_script]


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

    return True


def update_script_state(decoded_lic):
    enabled = 'active'
    # disabled = 'disabled'

    if decoded_lic['category'] == 'all_access':
        print(f'👑 - All Access Granted')
        for script in all_scripts:
            script.state = 'active'
    elif decoded_lic['category'] == 'package':
        print(f'📦 - Package Access')
    elif decoded_lic['category'] == 'individual':
        print(f'📃 - Individual Script')
        match (decoded_lic['name']):
            case 'kourend_crab_killer':
                kourend_crab_killer_script.state = enabled
            case 'cow_killer':
                cow_killer_script.btn_state = enabled
            case 'barb_fisher':
                barb_fisher_script.state = enabled
            case 'red_chin_hunter':
                red_chin_script.state = enabled
            case 'blast_furnace':
                blast_furance_script.state = enabled
            case 'black_lizards':
                black_lizards_script.state = enabled
            case 'dhide_bodies':
                dhide_bodies_script.state = enabled
            case 'tithe_farmer':
                tithe_farmer_script.state = enabled
    return
