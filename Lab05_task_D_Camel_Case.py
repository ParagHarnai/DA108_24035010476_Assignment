import re

inputCamelCase = ''
output_snake_case = ''
camelCasePattern = '[A-Z]{1,1}[a-z]*'
camelCaseStringList = []

while (inputCamelCase.lower() != 'q'):
    inputCamelCase = input(f"Enter an alphabetic variable name in camelCase: ")
    if (not inputCamelCase):
        print(f"No name is entered, try again!")
        continue
    if not inputCamelCase.isalpha():
        print(f"Name is not alphabetic, try again!")
        continue
    if inputCamelCase.lower() != 'q':
        re_p = re.compile(camelCasePattern)
        re_match = re_p.search(inputCamelCase)
        camelCaseStringList = re_p.findall(inputCamelCase)
        if not (camelCaseStringList):
            print(f"Entered string {inputCamelCase} is not in camel case, try again!")
        else:
            if re_match is not None:
                if re_match.start():
                    output_snake_case = inputCamelCase[0:re_match.start():1]
                for i_camelCase in camelCaseStringList:
                    output_snake_case = output_snake_case + '_' + i_camelCase.lower() if output_snake_case else output_snake_case + i_camelCase.lower()
                print(f"\nEntered camelCase name is: \'{inputCamelCase}\'\nNew snake_case name is: \'{output_snake_case}\'\n")
                output_snake_case = ''
