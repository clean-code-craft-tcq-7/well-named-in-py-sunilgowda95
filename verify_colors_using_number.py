from major_minor_colors_var import MAJOR_COLORS, MINOR_COLORS

def get_color_from_pair_number(pair_number):
  zero_based_pair_number = pair_number - 1
  major_index = zero_based_pair_number // len(MINOR_COLORS)
  if major_index >= len(MAJOR_COLORS):
    raise Exception('Major index out of range')
  minor_index = zero_based_pair_number % len(MINOR_COLORS)
  if minor_index >= len(MINOR_COLORS):
    raise Exception('Minor index out of range')
  return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]

def verify_colors_from_number(expected_major_color, expected_minor_color, pair_number):
  major_color, minor_color = get_color_from_pair_number(pair_number)
  assert major_color == expected_major_color, "major color is not matching with given pair number"
  assert minor_color == expected_minor_color, "minor color is not matching with given pair number"