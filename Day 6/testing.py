def reverse_digits(number):
    negative=number<0
    number=abs(number)
    reversed_number=int(str(number)[::-1])
    if negative:
        reversed_number*=-1
    return reversed_number


############
#TEST CASES#
############

#Test 1: 0
print("Testing 0")
if reverse_digits(0)==0:
    print('passed!')
else:
    print('failed')

#Test 2: Positive integer
print("\nTesting 172")
if reverse_digits(172)==271:
    print('passed!')
else:
    print('failed')

#Test 3: Negative Integer
print("\nTesting -152")
if reverse_digits(-152)==-251:
    print('passed!')
else:
    print('failed')

