import re
# Don't forget to run your tests!

def is_character_match(string1, string2):
	array_of_letters_left = [x for x in string1.lower()]
	array_of_letters_right =[x for x in string2.lower()]
	for element in array_of_letters_left:
		if not element in array_of_letters_right:
			return False
		array_of_letters_right.remove(element)
	return True