from colors_pairs import get_color_from_pair_number

def test_colors_from_number(expected_major_color, expected_minor_color, pair_number):
  major_color, minor_color = get_color_from_pair_number(pair_number)
  assert major_color == expected_major_color, "major color is not matching with given pair number"
  assert minor_color == expected_minor_color, "minor color is not matching with given pair number"