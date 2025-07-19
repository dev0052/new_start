''' Create a simple login system. Store usernames and passwords in a dictionary.
    Ask the user for their username and password.
    If they match a pair in the dictionary, print "Access granted". Otherwise, print "Access denied" '''


users = {
    "admin": "password123",
    "user1": "pass"
}

username = input("Enter username: ")
password = input("Enter password: ")

# Check if username exists and if the password matches
if username in users and users[username] == password:
    print("Access granted!")
else:
    print("Access denied!")