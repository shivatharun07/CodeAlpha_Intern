username = input("Enter username: ")

query = "SELECT * FROM users WHERE username = '" + username + "'"
print("Executing query:", query)

