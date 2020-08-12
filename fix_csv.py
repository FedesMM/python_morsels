import sys

file_input_name = sys.argv[1]
file_output_name = sys.argv[2]
delimiter = '|'
quote = "'"

file_input = open(file_input_name, "r")
old_text = file_input.read()
file_input.close()
print(old_text)


new_text = old_text.replace(delimiter, ",")
print(new_text)
file_output = open(file_output_name, "r")
file_output.write(new_text)
file_output.close()

