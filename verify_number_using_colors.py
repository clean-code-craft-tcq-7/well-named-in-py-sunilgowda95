from major_minor_colors_var import MAJOR_COLORS, MINOR_COLORS

def get_pair_number_from_color(major_color, minor_color):
  try:
    major_index = MAJOR_COLORS.index(major_color)
  except ValueError:
    raise Exception('Major index out of range')
  try:
    minor_index = MINOR_COLORS.index(minor_color)
  except ValueError:
    raise Exception('Minor index out of range')
  return major_index * len(MINOR_COLORS) + minor_index + 1

def verify_number_from_colors(expected_pair_number, major_color, minor_color):
  pair_number = get_pair_number_from_color(major_color, minor_color)
  assert pair_number == expected_pair_number, "pair number is not matching with given pair of colors"