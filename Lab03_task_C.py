# Lab 03 Task 03
user_input_string = ''
output_list = []
output_string = ''
while (user_input_string != 'q'):
    user_input_string = str(input("user input: "))
    if (user_input_string == 'q'):
        break
    if not user_input_string:
        continue
    output_list = user_input_string.split(' ')
    if output_list:
        for i_str in output_list:
            if len(i_str) > 1:
                output_string = output_string + " " + i_str.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')\
                .replace('A', '').replace('E', '').replace('I', '').replace('O', '').replace('U', '')
            elif len(i_str) == 1:
                output_string = output_string + " " + i_str
    print("output: ", output_string)
