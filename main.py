from verify_number_using_colors import verify_number_from_colors
from verify_colors_using_number import verify_colors_from_number
from colour_coding_reference_manual import print_manual

if __name__ == '__main__':
  verify_number_from_colors(4, 'White', 'Brown')
  verify_number_from_colors(5, 'White', 'Slate')
  verify_colors_from_number('Black', 'Orange', 12)
  verify_colors_from_number('Violet', 'Slate', 25)
  verify_colors_from_number('Red', 'Orange', 7)
  print_manual()
  print('Done :)')