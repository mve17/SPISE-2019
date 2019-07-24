#This program assumes the entered text only contains letters and spaces
alphabet='abcdefghijklmnopqrstuvwxyz'

encrypt_decrypt=input("Would you like to encode or decode? [e/d] ")

if encrypt_decrypt=='e':

	plain_text=input('Please enter text to encrypt: ').lower()
	shift=int(input('Please enter encryption shift: '))

	encrypted_text=''
	for char in plain_text:#one convenient way to do the shift is to use ascii values 
		if char==' ':
			encrypted_text+=' '
		else:
			char_index=alphabet.index(char)
			new_char_index=(char_index+shift)%len(alphabet)
			encrypted_text+=alphabet[new_char_index]
	print('\n')
	print(encrypted_text)	

else:
	encrypted_text=input('Please enter text to decrypt: ').lower()
	print('\n')
	print('printing all possible decryptions...')
	for shift in range(26):
		possible_decrypt=''
		for char in encrypted_text:
			if char==' ':
				possible_decrypt+=' '
			else:
				char_index=alphabet.index(char)
				new_char_index=(char_index+shift)%len(alphabet)
				possible_decrypt+=alphabet[new_char_index]
		print(possible_decrypt)
