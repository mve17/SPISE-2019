import random

TRIALS=10000

running_total=0
for i in range(TRIALS):
    count=0
    while count<=1:
        count+=random.random()
    running_total+=count
    
average_count=running_total/TRIALS
print('Estimated Solution:',average_count)
print('The exact answer is e/2')
