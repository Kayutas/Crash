# List of current usernames
current_users = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']

# List of new usernames to check
new_users = ['alice', 'Frank', 'Charlie', 'George', 'bob']

# Convert current_users to lowercase for case-insensitive comparison
current_users_lower = [user.lower() for user in current_users]

# Loop through each username in new_users and check if it's available
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please choose a different username.")
    else:
        print(f"The username '{new_user}' is available.")


numbers = list(range(1, 10))  # Store numbers 1 through 9 in a list

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")