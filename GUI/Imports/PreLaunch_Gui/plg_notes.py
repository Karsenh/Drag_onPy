class PlgScriptData:
    def __init__(self, name, requirements, known_issues, rtr, options):
        self.name = name
        self.requirements = requirements
        self.known_issues = known_issues
        self.rtr = rtr
        self.options = options


def get_plg_data():
    point = '\u2022'

    plg_notes = [
        PlgScriptData("Ardy_Knights",
                requirements=f"{point} Splasher - Join 'SplashWords' cc to find world.\n"
                             f"{point} Full Rogue outfit (Rogues Den MiniGame).\n"
                             f"{point} Food tab containing (Lobs, Monks, Tuna, Wine)",
                      known_issues=f"{point} Stops without Splasher.\n"
                             f"{point} Stops if knight moves out of the 2 northern most bank tiles.",
                rtr=f"⭐⭐⭐\n"
                    f"4-5 hrs. (avg.)\n"
                    f"Limited by Splasher time",
                options=["Dodgy Necklace", ""]),
        PlgScriptData("Cow_Killer",
                requirements=f"{point} Splasher - Join 'SplashWords' cc to find world.\n"
                             f"{point} Full Rogue outfit (Rogues Den MiniGame).",
                known_issues=f"{point} Stops without Splasher.\n"
                             f"{point} Stops if knight moves out of the 2 northern most bank tiles.",
                rtr=f"⭐⭐⭐\n"
                    f"4-5 hrs. (avg.)\n"
                    f"Limited by Splasher time",
                options=["test1"]),
    ]
    return plg_notes