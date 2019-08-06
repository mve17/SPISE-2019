import random

initial_valuation=50 #start with value $50
step_size=1 #$1 up and down
chance_up=.4
chance_down=.6

TRIALS=10000

count_get_to_100=0
for i in range(TRIALS):
    value=initial_valuation
    while value!=0 and value!=100:
        if random.random()<chance_up:
            value+=step_size
        else:
            value-=step_size
    if value==100:
        count_get_to_100+=1

print('Chance of getting to $100:',count_get_to_100/TRIALS)

#matplotlib code omitted, not hard using the template from lecture 5 notes
