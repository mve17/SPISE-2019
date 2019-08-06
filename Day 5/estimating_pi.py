import random

TRIALS=100000

count_in_circle=0
for i in range(TRIALS):
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    if x**2+y**2<=1:
        count_in_circle+=1
        
fraction_in_circle=count_in_circle/TRIALS #expect to be ~pi/4
print('Pi Estimate:',4*fraction_in_circle) 
