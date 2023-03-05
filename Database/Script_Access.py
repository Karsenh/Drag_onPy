import jwt

from Database.Connection import update_user_licenses, AUTHED_USER


class ScriptAccess:
    def __init__(self, btn_state):
        self.btn_state = btn_state


initial_state = 'disabled'

kourend_crab_killer_script = cow_killer_script = pisc_iron_script = \
    barb_fisher_script = red_chins_script = motherlode_mine_script = \
    blast_furance_script = black_lizards_script = dhide_bodies_script = \
    tithe_farmer_script = gnome_agility_script = canifis_rooftops = seers_rooftops \
    = rogue_cooker_script = ge_glass_blower_script = poh_tables_script = poh_larders_script \
    = hosidius_plough_script = ge_sulphurous_fertilizer_script = tithe_farmer_script \
    = draynor_shrimp_script = barb_trout_script = barb_fishing_script = ge_dart_fletcher_script \
    = ge_log_burner_script = crimson_swift_script = cerulean_twitches \
    = desert_lizards_script = red_lizards_script = draynor_man_script \
    = ardy_cake_script = hosidius_fruit_script = ardy_knight_script \
    = chop_fletcher_script = sw_teaks_script = cwars_lavas_script \
    = gilded_altar_script = edge_gold_script = unf_pots_script \
    = cball_smithing_script \
    = ScriptAccess(initial_state)

all_scripts = [kourend_crab_killer_script, cow_killer_script, pisc_iron_script,
               barb_fisher_script, red_chins_script, motherlode_mine_script,
               blast_furance_script, dhide_bodies_script, gnome_agility_script,
               canifis_rooftops, seers_rooftops, rogue_cooker_script,
               ge_glass_blower_script, hosidius_plough_script, ge_sulphurous_fertilizer_script,
               tithe_farmer_script, draynor_shrimp_script, barb_trout_script,
               barb_fishing_script, ge_dart_fletcher_script, ge_log_burner_script,
               crimson_swift_script, cerulean_twitches, desert_lizards_script,
               red_lizards_script, draynor_man_script, ardy_cake_script,
               hosidius_fruit_script, ardy_knight_script, chop_fletcher_script,
               sw_teaks_script, cwars_lavas_script, gilded_altar_script,
               edge_gold_script, unf_pots_script, cball_smithing_script]


def set_script_access(user_email, user_licenses):
    print(f"set_script_access 🔥'ed - user_licenses: {user_licenses}")

    updated_lic_arr = []
    used_licenses_arr = []

    for lic in user_licenses:
        print(f'Decoding License and setting Script Access for license: {lic}')

        JWT_SEC = 'cFnLPysgeQ6mLn83qVYz1PkNbJuZJzVyKkfv0kOfAKJ6Ihg6j0BUxIntWgIex5vAGDzb8DmYCLo2eaBa'

        try:
            decoded_lic = jwt.decode(lic, JWT_SEC, algorithms=["HS256"])
            print(f'Successfully decoded_lic: {decoded_lic}')
            # TODO: Check if license is already in a user session - skip if so, otherwise update_script_state & used_licenses_arr with curr license
            update_script_state(decoded_lic)
            updated_lic_arr.append(lic)
        except Exception:
            print(f'decoded token is invalid - likely expired. Remove from user doc with exception: {Exception}')

    # license_obj = json.load(license)
    update_user_licenses(user_email, updated_lic_arr)
    # TODO: Update user sessions with used_licenses_arr

    if not updated_lic_arr:
        print(f'⛔ Found licenses but they were expired. No more licenses to check.')
        return False

    return True


def update_script_state(decoded_lic):
    enabled = 'normal'
    # disabled = 'disabled'

    if decoded_lic['category'] == 'all_access':
        print(f'👑 - All Access Granted')
        for script in all_scripts:
            script.btn_state = 'normal'

    elif decoded_lic['category'] == 'package':
        print(f'📦 - Package Access')

    elif decoded_lic['category'] == 'individual':
        print(f'📃 - Individual Script')
        match (decoded_lic['name']):
            # Cases match token payload
            case 'kourend_crab_killer':
                kourend_crab_killer_script.state = enabled
            case 'cow_killer':
                cow_killer_script.btn_state = enabled
            case 'barb_fisher':
                barb_fisher_script.btn_state = enabled
            case 'blast_furnace':
                blast_furance_script.btn_state = enabled
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
            case 'crimson_swifts':
                crimson_swift_script.btn_state = enabled
            case 'cerulean_twitches':
                cerulean_twitches.btn_state = enabled
            case 'desert_lizards':
                desert_lizards_script.btn_state = enabled
            case 'red_lizards':
                red_lizards_script.btn_state = enabled
            case 'black_lizards':
                black_lizards_script.btn_state = enabled
            case 'red_chins':
                red_chins_script.btn_state = enabled
            case 'draynor_man':
                draynor_man_script.btn_state = enabled
            case 'ardy_cakes':
                ardy_cake_script.btn_state = enabled
            case 'hosidius_fruit':
                hosidius_fruit_script.btn_state = enabled
            case 'ardy_knights':
                ardy_knight_script.btn_state = enabled
            case 'chop_fletcher':
                chop_fletcher_script.btn_state = enabled
            case 'sw_teaks':
                sw_teaks_script.btn_state = enabled
            case 'cwars_lavas':
                cwars_lavas_script.btn_state = enabled
            case 'gilded_altar':
                gilded_altar_script.btn_state = enabled
            case 'edge_gold':
                edge_gold_script.btn_state = enabled
            case 'unf_pots':
                unf_pots_script.btn_state = enabled
            case 'cball_smither':
                cball_smithing_script.btn_state = enabled

    return
