

class PlgScriptOptions:
    def __init__ (self, script_name, options_arr):
        self.script_name = script_name
        self.options_arr = options_arr


class ScriptOption:
    def __init__ (self, option_name, option_value):
        self.name = option_name
        self.value = option_value


Global_Script_Options = PlgScriptOptions(None, [])
