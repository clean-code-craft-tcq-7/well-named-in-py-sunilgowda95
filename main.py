from test_number_using_colors import test_number_from_colors
from test_colors_using_number import test_colors_from_number
from colour_coding_reference_manual import print_manual

if __name__ == '__main__':
  test_number_from_colors(4, 'White', 'Brown')
  test_number_from_colors(5, 'White', 'Slate')
  test_colors_from_number('Black', 'Orange', 12)
  test_colors_from_number('Violet', 'Slate', 25)
  test_colors_from_number('Red', 'Orange', 7)
  print_manual()
  print('Done :)')