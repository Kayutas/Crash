fruit = 'apple'
print("is fruit == 'apple'? I predict True.")
print(fruit == 'apple')

print("is fruit == 'banana'? I predict False.")
print(fruit == 'banana')

print("\nIs fruit == orangere? I predict False.")
print(fruit == 'orange')    

# String equality and inequality
fruit = 'apple'
print("Is fruit == 'apple'? I predict True.")
print(fruit == 'apple')  # Expected output: True

print("\nIs fruit != 'banana'? I predict True.")
print(fruit != 'banana')  # Expected output: True

print("\nIs fruit == 'orange'? I predict False.")
print(fruit == 'orange')  # Expected output: False

# Tests using the lower() method
animal = 'Tiger'
print("\nIs animal.lower() == 'tiger'? I predict True.")
print(animal.lower() == 'tiger')  # Expected output: True

print("\nIs animal.lower() == 'lion'? I predict False.")
print(animal.lower() == 'lion')  # Expected output: False

# Numerical tests
age = 25
print("\nIs age == 25? I predict True.")
print(age == 25)  # Expected output: True

print("\nIs age != 30? I predict True.")
print(age != 30)  # Expected output: True

print("\nIs age > 20? I predict True.")
print(age > 20)  # Expected output: True

print("\nIs age < 20? I predict False.")
print(age < 20)  # Expected output: False

print("\nIs age >= 25? I predict True.")
print(age >= 25)  # Expected output: True

print("\nIs age <= 30? I predict True.")
print(age <= 30)  # Expected output: True

# Tests using and/or keywords
height = 6
weight = 150

print("\nIs height > 5 and weight > 100? I predict True.")
print(height > 5 and weight > 100)  # Expected output: True

print("\nIs height < 5 or weight > 100? I predict True.")
print(height < 5 or weight > 100)  # Expected output: True

print("\nIs height < 5 and weight > 100? I predict False.")
print(height < 5 and weight > 100)  # Expected output: False

print("\nIs height > 5 or weight < 100? I predict True.")
print(height > 5 or weight < 100)  # Expected output: True

# Test whether an item is in a list
favorite_fruits = ['apple', 'banana', 'grape']
print("\nIs 'apple' in favorite_fruits? I predict True.")
print('apple' in favorite_fruits)  # Expected output: True

print("\nIs 'orange' in favorite_fruits? I predict False.")
print('orange' in favorite_fruits)  # Expected output: False

# Test whether an item is not in a list
print("\nIs 'kiwi' not in favorite_fruits? I predict True.")
print('kiwi' not in favorite_fruits)  # Expected output: True

print("\nIs 'banana' not in favorite_fruits? I predict False.")
print('banana' not in favorite_fruits)  # Expected output: False
