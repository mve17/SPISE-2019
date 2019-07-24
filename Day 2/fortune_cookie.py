import random

noun_file=open('nouns.txt','r')
noun_list=noun_file.read().split('\n')
noun_file.close()

verb_file=open('verbs.txt','r')
verb_list=verb_file.read().split('\n')
verb_file.close()

adjective_file=open('adjectives.txt','r')
adjective_list=adjective_file.read().split('\n')
adjective_file.close()

#My format is going to be: "Good news! Your [noun] is taking a [ajective] [verb] for the better!"

user_wants_fortunes=True
while user_wants_fortunes:
	rand_adj=random.choice(adjective_list)
	rand_noun=random.choice(noun_list)
	rand_verb=random.choice(verb_list)
	print('Good news! Your',rand_noun,'is taking a',rand_adj,rand_verb,'for the better!')
	
	another_fortune=input('would you like another fortune? [y/n]')
	if another_fortune=='n':
		  user_wants_fortune=False

