#Opening the file with command

with open('fileprocessor1.py', 'r') as file:
	lines = file.readlines()

	print("Printing our User Data:\n")

	for line in lines:
		if line.startswith("#") or line.strip() == "":
			continue

	data = line.strip().split(":")

	username = str(input())
	password = str(input())
	userid = str(input())
	groupid = str(input())
	print(f"The user {username} has a password of {password} and has userid {userid} and groupid {groupid}")
