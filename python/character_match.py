import re
# Don't forget to run your tests!

def is_character_match(string1, string2):
	"""
	string1 is one string to compare
	string2 is another string to compare with string1
	return true if all elements exist within the compared string
	"""
	# We initialize 2 string array variables and set them to lower case for ease of comparison
	array_of_letters_left = [x for x in string1.lower()]
	array_of_letters_right =[x for x in string2.lower()]
	# Loop through one string array
	for element in array_of_letters_left:
		# At each index we ask if the element doesn't exist in the compared string so we can close out
		if not element in array_of_letters_right:
			# An element doesn't exist so return false
			return False
		# We've compared and concluded that the element exists in both arrays, so let's remove the element
		array_of_letters_right.remove(element)
	# We made it through both strings, return true
	return True