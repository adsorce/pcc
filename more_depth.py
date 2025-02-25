# Working with List Comprehension
evens = [number for number in range(2,11,2)]
print(evens)
print("\n------------------------------")

# Nesting
    # Lists in Dictionaries
pizza = {
    'crust': 'thin',
    'toppings': ['pepperoni', 'sausage', 'bacon', 'peppers']
    }
print(f"You ordered a {pizza['crust']} crust pizza "
    "with the following toppings:")

for options in pizza['toppings']:
    print(options)
print("\n------------------------------")

    # Lists in Dictionaries with Conditionals
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    }

for names, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{names.title()}'s favorite language is:")
        for language in languages:
            print(language.title())
    else:
        print(f"\n{names.title()}'s favorite languages are:")
        for language in languages:
            print(language.title())
print("\n------------------------------")

    # Dictionaries in Lists
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
print("\n------------------------------")

    # Dictionaries in Dictionaries
users = {
    "user_001": {"name": "Alice", "age": 25, "city": "New York"},
    "user_002": {"name": "Bob", "age": 30, "city": "San Francisco"},
    "user_003": {"name": "Charlie", "age": 35, "city": "Chicago"}
}

# Access a specific user's data
print(users["user_001"]["name"])  # Output: Alice
print(users["user_002"]["city"])  # Output: San Francisco