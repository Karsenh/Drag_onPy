class PlgNote:
    def __init__(self, name, requirements, known_issues, rtr):
        self.name = name
        self.requirements = requirements
        self.known_issues = known_issues
        self.rtr = rtr


def get_plg_notes():
    point = '\u2022'

    plg_notes = [
        PlgNote("Ardy_Knights",
                requirements=f"{point} Splasher - Join 'SplashWords' cc to find world.\n"
                             f"{point} Full Rogue outfit (Rogues Den MiniGame).",
                known_issues=f"{point} Stops without Splasher.\n"
                             f"{point} Stops if knight moves out of the 2 northern most bank tiles.",
                rtr=f"⭐⭐⭐\n"
                    f"4-5 hrs. (avg.)\n"
                    f"Limited by Splasher time"),
        PlgNote("Cow_Killer",
                requirements=f"{point} Cow Killer - Join 'SplashWords' cc to find world.\n{point} Full Rogues outfit.",
                known_issues=f"{point} Stops without Splasher.\n{point} Stops if Knight moves from 2 tiles against North bank wall.",
                rtr=f"⭐⭐⭐\n(2-3hrs avg.)"),
    ]
    return plg_notes