import random

def flip_coins(n): 
	# Returns a string of n coin flips, like 'HTTHTHHH...HT'
	coin_tosses = ''
	for i in range(n):
		# random.choice() takes in a list and returns a random element from it
		coin_tosses += random.choice(['H', 'T']) 
	return coin_tosses

def compute_longest_run(coin_tosses): 
	# coin_tosses should be a string as output by flip_coins(). 
	# Returns the length of the longest run
	
	# The procedure is to scan through the string, counting each run length
	longest_run_length = 1
	current_index = 0
	current_run_length = 1
	while current_index <= len(coin_tosses) - 2:
		# If next letter is the same, increment current run length
		if coin_tosses[current_index + 1] == coin_tosses[current_index]: 
			current_run_length += 1
			if current_run_length > longest_run_length:
				longest_run_length = current_run_length
		else:
			current_run_length = 1
		current_index += 1
	return longest_run_length

def collect_longest_run_data(coin_flips_per_trial,num_trials): 
	'''
	returns an array of length coin_flips_per_trial, where the element 
	at index i is the number of times the longest run was of length i+1.
	'''	
	output_array = coin_flips_per_trial * [0]
	for i in range(num_trials):
		coin_toss_sequence = flip_coins(coin_flips_per_trial)
		longest_run = compute_longest_run(coss_toss_sequence)
		output_array[longest_run - 1] += 1
	return output_array
