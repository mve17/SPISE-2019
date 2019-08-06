###########
#DEBUG IT!#
###########

#List Sort
unsorted_list = [6,2,5,1,3]
unsorted_list.sort()
sorted_list=unsorted_list
for i in range(len(unsorted_list)):
    print(sorted_list[i])

#Printing Dots
smallnumberfromuser = int(input('Enter a number between 0 and 20: '))
smallnumberfromuser = smallnumberfromuser * 2
for i in range(int(smallnumberfromuser / 2)):
    print('.')

#Genotype-to-Phenotype Dictionary
geno_to_pheno = {('long', 'long'): 'long', ('long', 'short'): 'long',
                 ('short', 'long'): 'long',('short','short'):'short'}

##############
#DEBUG IT! v2#
##############
import random
import time

difficulty=0
max_word_size=6
max_paragraph_size=10

lower_letters='abcdefghijklmnopqrstuvwxyz'
upper_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numerals='1234567890'
symbols='''!@#$%^&*()_+`~-=[]{}\|:;"'/?><.,'''
difficulty_ranking=[lower_letters,upper_letters,numerals,symbols]

def generate_letter():
    level=random.randint(0,difficulty)
    character=random.choice(difficulty_ranking[level])
    return character

def generate_word():
    word_size=random.randint(1,10)
    output=''
    for x in range(word_size):
        output+=generate_letter()
    return output

def generate_paragraph():
    par_size=random.randint(10,max_paragraph_size)
    output=''
    for x in range(0,par_size):
        output+=generate_word()
        output+=' '
    return output

def words_correct(attempt,solution):
    attempt_words=attempt.split(' ')
    solution_words=solution.split(' ')
    num_words_compare=min(len(attempt_words),len(solution_words))
    words_correct=0
    total_words=len(solution_words)
    for word_idx in range(0,num_words_compare):
        if attempt_words[word_idx]==solution_words[word_idx]:
            words_correct+=1
    return len(attempt_words),words_correct,total_words

def play_game():
    playing=True
    print('Get Ready to Type!\n')
    time.sleep(1)
    while playing:
        new_par=generate_paragraph()
        print(new_par+'\n')
        
        start=time.time()
        submission=input('type the above!\n')
        end=time.time()

        total_time=(end-start)/60
        words_typed,word_score,total_words=words_correct(submission,new_par)
        word_accuracy=round(word_score/total_words,3)
        wpm=round(words_typed/total_time,2)
        
        print('you typed at',wpm,'wpm with an accuracy of',word_accuracy,'!\n')

        keep_going=input('keep playing? (y/n)\n')
        if keep_going!='y':
            playing=False

play_game()
