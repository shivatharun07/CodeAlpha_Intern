username = input("Enter username: ")

query = "SELECT * FROM users WHERE username = %s"
values = (username,)

print("Executing secure query:", query)
