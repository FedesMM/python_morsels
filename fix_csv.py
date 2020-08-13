import sys

file_input_name = sys.argv[1]
file_output_name = sys.argv[2]
delimiter = '|'
quote = "'"

file_input = open(file_input_name, "r")
old_text = file_input.read()
file_input.close()
print("file_input: \n"+str(old_text))

new_text = old_text.replace("\',", ",")
new_text = new_text.replace(r'/[^\']?,/', ",")
print("\nfile_output: \n"+str(new_text))
file_output = open(file_output_name, "w")
file_output.write(new_text)
file_output.close()

