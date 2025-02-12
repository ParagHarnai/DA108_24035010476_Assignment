import re

input_long_message = ''
output_short_message = ''
short_pattern = '[a-ae-eo-oi-iu-u]+'
short_pattern_space = '[ ]{2, 2}'

while (input_long_message.lower() != 'q'):
    input_long_message = input(f"Enter a string with vowels or q to exit: ")
    if (not input_long_message):
        print(f"No string is entered, try again!")
        continue
    if input_long_message.lower() != 'q':
        re_p = re.compile(short_pattern, re.IGNORECASE)
        re_match = re_p.search(input_long_message)
        if re_match is not None:
            output_short_message = input_long_message
            while (re_match is not None) and (re_match.group()):
                output_short_message = output_short_message.replace(re_match.group(), '')
                re_match = re_p.search(output_short_message)
            output_short_message = output_short_message.replace('  ', ' ')
            output_short_message = output_short_message.strip()
            if not (output_short_message):
                print(f"Entered string \'{input_long_message}\' is empty or has only vowels, try again!")
            else:
                print(f"\nEntered string is: \'{input_long_message}\'\nNew short string is: \'{output_short_message}\'\n")
                output_short_message = ''
