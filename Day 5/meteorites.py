import random

TRIALS=10000
close_distance=1 #can set to 1/2 for 1/2 mile case

count_close=0
for i in range(TRIALS):
    x_1=random.uniform(0,1)
    y_1=random.uniform(0,2)
    x_2=random.uniform(0,1)
    y_2=random.uniform(0,2)
    if (x_1-x_2)**2+(y_1-y_2)**2<=close_distance**2:
        count_close+=1
        
print('Approximate Solution:',count_close/TRIALS)
