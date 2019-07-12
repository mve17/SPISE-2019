# Matt's String Library
# Provides two commands to do fun things with strings
def rotate_string(string_input,rotation_amount): 
	# For example, a rotation of 'butterfly' by 2 gives 'lybutterfl', 
	# and a rotation of 8 gives 'utterflyb'
	string_output = ''
	current_letter_index = (len(string_input) - rotation_amount) % len(string_input)
	for i in range(len(string_input)):
		string_output += string_input[current_letter_index]
		current_letter_index = (current_letter_index + 1) % len(string_input)
	return string_output
def print_word_box(string_input):
	for i in range(len(string_input)):
		print(rotate_string(string_input,i))

if __name__=='__main__':
    print_word_box('alligator')
