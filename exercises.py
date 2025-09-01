# Exercise 1: List and Indexing
def manage_students():
    students = ['Ayah', 'Ghalia', 'Noor', 'Jannah']
    first_student = students[1]
    last_student = students[-1]

    return first_student, last_student
    
print('Exercise 1:', manage_students())



# Exercise 2: Loop and String Concatenation
def combine_foods():
    foods= ('Pizza', 'Taco', 'pasta', 'Burger')
    meal = ' '

    for food in foods:
        meal += food + ', '
    
    return meal.strip()

print('Exercise 2:', combine_foods())



# Exercise 3: Slicing Tuples
def slice_foods():
    foods= ('Pizza', 'Taco', 'pasta', 'Burger')
    last_two=foods[-2:]

    return last_two

print('Exercise 3:', slice_foods())



# Exercise 4: Dictionaries and String Formatting
def hometown_info():
    home_town={
        'city': 'Manama',
        'state': 'Capital',
        'population': 297502
    }

    home_town_message = 'I was born in {city}, {state} - population of {population}'.format(**home_town)

    return home_town_message

print('Exercise 4:', hometown_info())



# Exercise 5: Iterating Over Dictionary Items
def list_home_town_items():
    home_town={
        'city': 'Manama',
        'state': 'Capital',
        'population': 297502
    }

    home_town_items =[]

    for key, value in home_town.items():
        home_town_items.append(f'{key} = {value}')

    return home_town_items

print('Exercise 5:', list_home_town_items())



# Level-Up

# Exercise 6: Celebrate Students
def create_awesome_students():
    students = ['Ayah', 'Ghalia', 'Noor', 'Jannah']
    awesome_students = [f'{student} is awesome!' for student in students]

    return awesome_students

print('Exercise 6:', create_awesome_students())



# Exercise 7: Filter Foods
def filter_foods_with_a():
    foods = ('Pizza', 'Burger', 'Taco', 'pie', 'Pasta', 'Salad', 'Soup', 'Rice')
    foods_with_an_a = list(filter(lambda food: "a" in food.lower(), foods))

    return foods_with_an_a
# Call the function and print the result
print('Exercise 7:', filter_foods_with_a())