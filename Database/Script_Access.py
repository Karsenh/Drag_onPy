import jwt


class ScriptAccess:
    def __init__(self, btn_state):
        self.btn_state = btn_state


initial_state = 'disabled'

kourend_crab_killer_script = cow_killer_script = pisc_iron_script = \
    barb_fisher_script = red_chin_script = motherlode_mine_script = \
    blast_furance_script = black_lizards_script = dhide_bodies_script = \
    tithe_farmer_script = gnome_agility_script = canifis_rooftops = seers_rooftops \
    = rogue_cooker_script = ge_glass_blower_script = poh_tables_script = poh_larders_script \
    = hosidius_plough_script = ge_sulphurous_fertilizer_script = tithe_farmer_script \
    = draynor_shrimp_script = barb_trout_script = barb_fishing_script = ge_dart_fletcher_script \
    = ge_log_burner_script \
    = ScriptAccess(initial_state)

all_scripts = [kourend_crab_killer_script, cow_killer_script, pisc_iron_script,
               barb_fisher_script, red_chin_script, motherlode_mine_script,
               blast_furance_script, dhide_bodies_script, gnome_agility_script,
               canifis_rooftops, seers_rooftops, rogue_cooker_script,
               ge_glass_blower_script, hosidius_plough_script, ge_sulphurous_fertilizer_script,
               tithe_farmer_script, draynor_shrimp_script, barb_trout_script, barb_fishing_script,
               ge_dart_fletcher_script, ge_log_burner_script]


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
            script.btn_state = 'active'
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
                barb_fisher_script.btn_state = enabled
            case 'red_chin_hunter':
                red_chin_script.btn_state = enabled
            case 'blast_furnace':
                blast_furance_script.btn_state = enabled
            case 'black_lizards':
                black_lizards_script.btn_state = enabled
            case 'dhide_bodies':
                dhide_bodies_script.btn_state = enabled
            case 'gnome_course':
                gnome_agility_script.btn_state = enabled
            case 'canifis_rooftops':
                canifis_rooftops.btn_state = enabled
            case 'seers_rooftops':
                seers_rooftops.btn_state = enabled
            case 'rogue_cooker':
                rogue_cooker_script.btn_state = enabled
            case 'ge_glass_blower':
                ge_glass_blower_script.btn_state = enabled
            case 'poh_larders':
                poh_larders_script.btn_state = enabled
            case 'poh_tables':
                poh_tables_script.btn_state = enabled
            case 'hosidius_plough':
                hosidius_plough_script.btn_state = enabled
            case 'ge_sulphurous_fertilizer':
                ge_sulphurous_fertilizer_script.btn_state = enabled
            case 'tithe_farmer':
                tithe_farmer_script.btn_state = enabled
            case 'draynor_shrimp':
                draynor_shrimp_script.btn_state = enabled
            case 'barb_trout':
                barb_trout_script.btn_state = enabled
            case 'barb_fishing_script':
                barb_fishing_script.btn_state = enabled
            case 'ge_dart_fletcher':
                ge_dart_fletcher_script.btn_state = enabled
            case 'ge_log_burner':
                ge_log_burner_script.btn_state = enabled
    return
