# List of favorite fruits
favorite_fruits = ['mango', 'banana', 'strawberry']

# Five if statements to check for certain fruits
if 'mango' in favorite_fruits:
    print("You really like mangoes!")

if 'banana' in favorite_fruits:
    print("You really like bananas!")

if 'strawberry' in favorite_fruits:
    print("You really like strawberries!")

if 'apple' in favorite_fruits:
    print("You really like apples!")

if 'grape' in favorite_fruits:
    print("You really like grapes!")

# Cleaner version 

# List of favorite fruits
favorite_fruits = ['mango', 'banana', 'strawberry']

# List of fruits to check
fruits_to_check = ['mango', 'banana', 'strawberry', 'apple', 'grape']

# Loop through fruits_to_check and print a message if the fruit is in favorite_fruits
for fruit in fruits_to_check:
    if fruit in favorite_fruits:
        print(f"You really like {fruit}s!")
