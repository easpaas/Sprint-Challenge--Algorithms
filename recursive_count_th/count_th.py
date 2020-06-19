'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
	# input is a string
	substr = "th"

	# Base case
	# case1: empty input string
	# case2: length of input string is less that 'th'
	if (len(word) == 0 or len(word) < len(substr)): 
		return 0

    # Checking if the first substring matches 
	if (word[0 : 2] == substr):
		return 1 + count_th(word[1:])

	# Return the count from the remaining index 
	return count_th(word[1:])