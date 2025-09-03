# Exercise 0: Example
def example_list_function():
  example_list = ['element1', 'element2', 'element3']
  for element in example_list:
      print(element)

example_list_function()

# Exercise 1: List and Indexing
def manage_students():
    students = ['Ali', 'Ahmed', 'Alia']
    first_student = students[1]
    last_student = students[2] # or u can do students[-1]
    return first_student, last_student
print('Exercise 1:', manage_students())


# Exercise 2: Loop and String Concatenation
def combine_foods():
    foods = ('Pasta', 'Biryani', 'Risotto')
    meal = ''
    for food in foods:
        meal += food + " "   # add a space for readability
    return meal      # remove the last extra space

print("Exercise 2:", combine_foods())

# Exercise 3: Slicing Tuples
def slice_foods():
    foods = ('Pasta', 'Biryani', 'Risotto')
    last_two_foods = foods[-2:]
    return last_two_foods

print('Exercise 3:', slice_foods())

# Exercise 4: Dictionaries and String Formatting
def hometown_info():
    home_town = {
        'city':'Manama',
        'state':'Capital',
        'population':90000,
    }
    hometown_message = f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}"
    return hometown_message
print('Exercise 4:', hometown_info())

# Exercise 5: Iterating Over Dictionary Items
def list_home_town_items():
    home_town = {
        'city':'Manama',
        'state':'Capital',
        'population':'90000',
    }

    home_town_items = []
    for  key, value in home_town.items():
        home_town_items.append(f"{key} = {value}")
    return home_town_items
print('Exercise 5:', list_home_town_items())
