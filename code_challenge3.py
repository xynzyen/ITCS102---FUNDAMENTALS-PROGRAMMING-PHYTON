#set a name and password variable
#must login using the information both username & password should match
#if username and password match prompt message 'access granted' if not 'access denied'

username = "jhapikit"
password = "JhaYen102623"

user_input =  input("Welcome to the portal. Please type your username:")
pass_input = input("Please insert your password:")

if user_input == username and pass_input == password:
	print("Access Granted")
else: 
	print("Access Denied")