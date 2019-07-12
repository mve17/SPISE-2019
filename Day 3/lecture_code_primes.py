def check_prime(x):  # Checks if number x is prime. Returns True or False.
    if x < 1:
        return False
    else:
        for i in range(2, x):
            if x % i== 0:
                return False
        return True

def print_first_n_primes(n):
    primes_found = 0
    number_to_check = 2
    while primes_found < n:
        if check_prime(number_to_check) == True:
            print(number_to_check)
            primes_found += 1 #shorthand for primes_found=primes_found+1
        number_to_check += 1

print_first_n_primes(5)
