import os


def get_skill_level(skill_name="agility"):
    levels_txt_file_path = f'{os.getcwd()}\Assets\Levels.txt'

    search_skill = f'={skill_name}'

    search_line = ""

    with open(levels_txt_file_path, "r") as file:
        file_lines = file.readlines()
        for line in file_lines:
            if search_skill in line:
                print(f'Line contains skill_name: {line}')
                search_line = line
            # print(f'line: {line}')

    if search_line:
        trimmed_level = search_line.split('level=')[1].split(',')[0]
        print(f'trimmed_level = {trimmed_level}')
        return int(trimmed_level)

    else:
        return None
