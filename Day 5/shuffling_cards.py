import random

def check_all_out_of_order(deck):
    for i in range(len(deck)):
        if deck[i]==i:
            return False
    return True

TRIALS=10000

count_all_out_of_order=0
for i in range(TRIALS):
    deck=list(range(52))
    random.shuffle(deck)
    if check_all_out_of_order(deck):
        count_all_out_of_order+=1

print('Estimated Solution:',count_all_out_of_order/TRIALS)
print('Exact solution is roughly 1/e')
