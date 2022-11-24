from colors_pairs import get_pair_number_from_color

def test_number_from_colors(expected_pair_number, major_color, minor_color):
  pair_number = get_pair_number_from_color(major_color, minor_color)
  assert pair_number == expected_pair_number, "pair number is not matching with given pair of colors"