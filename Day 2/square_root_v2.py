x=float(input('Please enter number to take square root of: '))
guess=1
for time in range(1000):
	guess=.5*(guess+x/guess)
print(guess)
print('for comparison, the actual square root is:\n'+str(x**.5))
