favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',  
}

language = favorite_languages['sarah'].title()
language = favorite_languages['jen'].title()
print(f"Sarah's favorite language is {language}.")
print(f"Jen's favorite language is {language}.")   

# second try

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',  
}

sarah_language = favorite_languages['sarah'].title()
jen_language = favorite_languages['jen'].title()

print(f"Sarah's favorite language is {sarah_language}.")
print(f"Jen's favorite language is {jen_language}.")

# third try

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',  
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

