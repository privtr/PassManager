import os

def isUserValid(username, password):
	if os.path.isfile('data.txt'):
		file = open("data.txt", 'r')
		lines = file.readlines()
		file.close()
		flag = False
		for i in lines:
			index = i.find(',')
			i.replace('\n','')
			if username == i[:index] and password == i[index + 1:]:
				flag = True
				break
		if flag == True:
			return True
		else:
			return False
	else:
		print("Error: data file missing")

def isUserAvailable(username):
	pass
	