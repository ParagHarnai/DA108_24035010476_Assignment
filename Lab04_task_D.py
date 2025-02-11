input_username_1 = ''
input_username_2 = ''

while input_username_1 != 'q' or input_username_2 != 'q':
    input_username_1 = input("Enter string 1: ")
    input_username_2 = input("Enter string 2: ")
    if input_username_1 != 'q' and input_username_2 != 'q' and (input_username_1 or input_username_1):
        with open('Lab04_task_D_output.txt', 'wt+', encoding="utf-8") as f:
            if len(input_username_1) > len(input_username_2):
                print(f"String 1 - {input_username_1} is longer than string 2 - {input_username_2}.")
                output_string = f"String 1 - {input_username_1} is longer than string 2 - {input_username_2}."
            elif len(input_username_1) < len(input_username_2):
                print(f"String 2 - {input_username_2} is longer than string 1 - {input_username_1}.")
                output_string = f"String 2 - {input_username_2} is longer than string 1 - {input_username_1}."
            else:
                print(f"String 1 - {input_username_1} and string 2 - {input_username_2} have same length: {len(input_username_2)}.")
                output_string = f"String 1 - {input_username_1} and string 2 - {input_username_2} have same length: {len(input_username_2)}."
            f.write(output_string)
