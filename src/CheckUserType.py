import io
import csv

def checkUserType(userId):
	# determine the type of param passed in (either prof id or student id)
	usersCSV = open("Users.csv", "r")
	usersReader = csv.reader(usersCSV)
	userType = ''
	for row in usersReader:
		if row[0].strip() == str(userId):
			userType = row[5].strip()
			break
	usersCSV.close()
	# return 'S' for student, 'P' for professor
	return userType
