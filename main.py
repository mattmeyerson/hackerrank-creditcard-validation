import re


# Checks if card_number meets the following conditions
# - Starts with 4, 5, or 6
# - Contains only 16 digits, with or without hyphens separating the digits into 4 groups of 4
# - Doesn't contain 4 or more consecutively repeating digits
def validate_card_number(card_number):
    if re.search(r'^[456][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}$', card_number) is None:
        return False

    card_no_dashes = card_number.replace('-', '')

    if re.search(r'([0-9])\1{3}', card_no_dashes) is not None:
        return False

    return True


# Takes in Credit Card numbers from StdIN and validates them
if __name__ == '__main__':

    # The first input is an integer representing the number of credit card numbers to follow
    num_of_lines_str = input()

    if not num_of_lines_str.isdigit():
        raise ValueError('Expected an integer for the first line but received: ' + num_of_lines_str)

    num_of_lines = int(num_of_lines_str)
    if num_of_lines > 99 or num_of_lines < 1:
        raise ValueError('Expected the number of lines to be greater than 0 and less than 100')

    credit_card_validations = []
    for x in range(num_of_lines):
        credit_card_validations.append(validate_card_number(input()))

    for x in range(int(num_of_lines_str)):
        print('Valid' if credit_card_validations[x] else 'Invalid')
