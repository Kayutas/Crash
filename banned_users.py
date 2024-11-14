banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
    
# Testing variable definitions
car = 'subaru'
color = 'blue'
speed = 120
age = 5
price = 20000

# Test 1: car is 'subaru' (True)
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')  # Expected output: True

# Test 2: car is 'audi' (False)
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')  # Expected output: False

# Test 3: color is 'blue' (True)
print("\nIs color == 'blue'? I predict True.")
print(color == 'blue')  # Expected output: True

# Test 4: color is 'red' (False)
print("\nIs color == 'red'? I predict False.")
print(color == 'red')  # Expected output: False

# Test 5: speed > 100 (True)
print("\nIs speed > 100? I predict True.")
print(speed > 100)  # Expected output: True

# Test 6: speed < 100 (False)
print("\nIs speed < 100? I predict False.")
print(speed < 100)  # Expected output: False

# Test 7: age <= 10 (True)
print("\nIs age <= 10? I predict True.")
print(age <= 10)  # Expected output: True

# Test 8: age > 10 (False)
print("\nIs age > 10? I predict False.")
print(age > 10)  # Expected output: False

# Test 9: price == 20000 (True)
print("\nIs price == 20000? I predict True.")
print(price == 20000)  # Expected output: True

# Test 10: price < 15000 (False)
print("\nIs price < 15000? I predict False.")
print(price < 15000)  # Expected output: False

    