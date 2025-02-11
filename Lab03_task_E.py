# Lab 03 Task 05
DNA_input_string = 'ATGTACTC ATTCGTTTCG GAAGAGACAG GTACGTTAAT AGTTAATAGC GTACTTCTTT TTCTTGCTTT CGTGGTATTC TTGCTAGTTA CACTAGCCAT CCTTACTGCG CTTCGATTGT GTGCGTACTG CTGCAATATT GTTAACGTGA GTCTTGTAAA ACCTTCTTTT TACGTTTACT CTCGTGTTAA AAATCTGAAT TCTTCTAGAG TTCCTGATCT TCTGGTCTAA'
DNA_output_string = ''
DNA_string_list = DNA_input_string.split(' ')
DNA_len = len(DNA_string_list)
for i in range(DNA_len):
    DNA_string_list[i] = DNA_string_list[i][::-1]
    DNA_output_string = DNA_output_string + ' ' + str(DNA_string_list[i])
DNA_out_TTACT_count = DNA_output_string.count('TTACT')
DNA_in_TTACT_count = DNA_input_string.count('TTACT')
print("DNA string reversed: ", DNA_output_string)
print(f"Count of 'TTACT' in the input DNA string: {DNA_in_TTACT_count:5d}")
print("Count of 'TTACT' in the reversed DNA string: ", str(DNA_out_TTACT_count))
