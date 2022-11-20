from major_minor_colors_var import MAJOR_COLORS, MINOR_COLORS

def get_color_code_manual():
    color_code_pair_list = []
    for major_color in MAJOR_COLORS:
        for minor_color in MINOR_COLORS:
            color_code_pair_list.append([major_color, minor_color])
    return color_code_pair_list

def print_manual():
    color_code_manual = get_color_code_manual()
    for each_pair in color_code_manual:
        print(f'Pair no. {color_code_manual.index(each_pair)+1}, Major color is {each_pair[0]}, Minor color is {each_pair[1]}')