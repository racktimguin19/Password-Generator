import string
import random
from flask import request


# Generate Password according to the checkboxes filled by user
def generate_password(password_length):

    generated_password = ""

    # Storing all the characters in different variables
    uppercase_string = string.ascii_uppercase
    lowercase_string = string.ascii_lowercase
    numbers_string = string.digits
    symbol_string = string.punctuation

    # Variable to store the combined list of characters (including uppercase, lowercase, digits, symbols) based on user requirements
    combined_list = []

    '''
    Character list for all the possible combination
        1. Exclusively each type of character
        2. All combination with Uppercase
        3. All combination with Lowercase
        4. All combination with Numbers
        5. All combination with Symbols
    '''
    only_uppercase = list(uppercase_string)
    only_lowercase = list(lowercase_string)
    only_numbers = list(numbers_string)
    only_symbols = list(symbol_string)

    uppercase_lowercase = list(uppercase_string) + list(lowercase_string)
    uppercase_numbers = list(uppercase_string) + list(numbers_string)
    uppercase_symbols = list(uppercase_string) + list(symbol_string)

    lowercase_numbers = list(lowercase_string) + list(numbers_string)
    lowercase_symbols = list(lowercase_string) + list(symbol_string)

    numbers_symbols = list(numbers_string) + list(symbol_string)

    uppercase_lowercase_numbers = list(uppercase_string) + list(lowercase_string) + list(numbers_string)
    uppercase_lowercase_symbols = list(uppercase_string) + list(lowercase_string) + list(symbol_string)
    uppercase_numbers_symbols = list(uppercase_string) + list(numbers_string) + list(symbol_string)
    lowercase_numbers_symbols = list(lowercase_string) + list(numbers_string) + list(symbol_string)

    uppercase_lowercase_numbers_symbols = list(uppercase_string) + list(lowercase_string) + list(numbers_string) + list(symbol_string)



    if request.method == 'POST':
    # Checking the checkboxes if the user wants uppercase, lowercase, numbers and symbols in their password
        checkbox_uppercase = bool(request.form.get('uppercase'))
        checkbox_lowercase = bool(request.form.get('lowercase'))
        checkbox_numbers = bool(request.form.get('numbers'))
        checkbox_symbols = bool(request.form.get('symbols'))
        checkbox_select_all = bool(request.form.get('all'))

        '''
        Total Checkbox checked count,
        If 0, then generating error message
        '''
        length_checkbox = checkbox_uppercase + checkbox_lowercase + checkbox_numbers + checkbox_symbols + checkbox_select_all

        if length_checkbox == 0:
            generated_password = "You must select at least one checkbox!"

            return generated_password

        # Conditions for the characters needed by user

        # If all parameters are selected
        elif checkbox_select_all:
            combined_list = uppercase_lowercase_numbers_symbols

        # Only one parameter selection
        elif checkbox_uppercase and not checkbox_lowercase and not checkbox_numbers and not checkbox_symbols:
            combined_list = only_uppercase
        elif checkbox_lowercase and not checkbox_uppercase and not checkbox_numbers and not checkbox_symbols:
            combined_list = only_lowercase
        elif checkbox_numbers and not checkbox_uppercase and not checkbox_lowercase and not checkbox_symbols:
            combined_list = only_numbers
        elif checkbox_symbols and not checkbox_uppercase and not checkbox_lowercase and not checkbox_numbers:
            combined_list = only_symbols
        
        # Two parameter selsection
        elif checkbox_uppercase and checkbox_lowercase and not checkbox_numbers and not checkbox_symbols:
            combined_list = uppercase_lowercase
        elif checkbox_uppercase and checkbox_numbers and not checkbox_lowercase and not checkbox_symbols:
            combined_list = uppercase_numbers
        elif checkbox_uppercase and checkbox_symbols and not checkbox_lowercase and not checkbox_numbers:
            combined_list = uppercase_symbols
        elif checkbox_lowercase and checkbox_numbers and not checkbox_uppercase and not checkbox_symbols:
            combined_list = lowercase_numbers
        elif checkbox_lowercase and checkbox_symbols and not checkbox_uppercase and not checkbox_numbers:
            combined_list = lowercase_symbols
        elif checkbox_numbers and checkbox_symbols and not checkbox_uppercase and not checkbox_lowercase:
            combined_list = numbers_symbols

        # Three parameter selection    
        elif checkbox_uppercase and checkbox_lowercase and checkbox_numbers and not checkbox_symbols:
            combined_list = uppercase_lowercase_numbers
        elif checkbox_uppercase and checkbox_lowercase and checkbox_symbols and not checkbox_numbers:
            combined_list = uppercase_lowercase_symbols
        elif checkbox_uppercase and checkbox_numbers and checkbox_symbols and not checkbox_lowercase:
            combined_list = uppercase_numbers_symbols
        elif checkbox_lowercase and checkbox_numbers and checkbox_symbols and not checkbox_uppercase:
            combined_list = lowercase_numbers_symbols
        
        else:
            combined_list = uppercase_lowercase_numbers_symbols
            

    # Shuffeling all the characters
    random.shuffle(combined_list)

    generated_password = "".join(combined_list[:password_length])

    return generated_password


if __name__ == "__main__":
    generate_password()
