from random import randint

def generatePassword(length, spec_char):
	lenPass = length
	specChar_use = spec_char
	password = ''
	spec_char = ['!', '@', '#', '_']
	norm_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
				 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
				 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
				 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
				 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
				 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
				 '8', '9']
	if specChar_use == True:
		while len(password) <= lenPass:
			random_num = randint(0, 8)
			if random_num <= 1:
				random_num = randint(0, 3)
				password = password + spec_char[random_num]
			else:
				random_num = randint(0, 61)
				password = password + norm_char[random_num]
	else:
		while len(password) <= lenPass:
			random_num = randint(0, 61)
			password = password + norm_char[random_num]

	print(password)


generatePassword(15, True)
generatePassword(15, False)
	