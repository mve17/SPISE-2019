txt_file=open('words.txt','r')
word_data=txt_file.read()
txt_file.close()
word_list=word_data.split('\n')

write_file=open('15_letter_words.txt','w')
for word in word_list:
	if len(word)==15:
		write_file.write(word+'\n')
		

