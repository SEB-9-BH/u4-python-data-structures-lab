# Exercise 0: Example
#
# This is a practice exercise to familiarize you with basic Python data structures.
#
# Create a list called `example_list` and append three elements to it. Print each element using a loop.
#
# Requirements:
# - The list should contain any three elements of your choice.
# - Use a loop to print each element.

def example_list_function():
  example_list = ['element1', 'element2', 'element3']
  for element in example_list:
      print(element)

# Call the function and print each element
example_list_function()

# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

def manage_students():
    students = ["Alice", "Bob", "Charlie", "Diana", "Emma"]
    first_student = students[1]  # Second student (index 1)
    last_student = students[-1]  # Last student (negative indexing)
    
    return {
        'students': students,
        'first_student': first_student,
        'last_student': last_student
    }

# Call the function and print the result
print('Exercise 1:', manage_students())

# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.

def combine_foods():
    # Get students list from previous function to ensure same number of items
    students = ["Alice", "Bob", "Charlie", "Diana", "Emma"]
    foods = ("pizza", "burger", "salad", "pasta", "sandwich")  # Same number as students
    
    meal = ""
    for food in foods:
        meal += food + " "
    
    # Remove trailing space
    meal = meal.strip()
    
    return {
        'foods': foods,
        'meal': meal
    }
# Call the function and print the result
print('Exercise 2:', combine_foods())

# Exercise 3: Slicing Tuples
#
# Using the slice operator, assign a new tuple containing only the last two food strings in the foods to a variable named last_two_foods.

def slice_foods():
    foods = ("pizza", "burger", "salad", "pasta", "sandwich")
    last_two_foods = foods[-2:]  # Get last two items using slice operator
    
    return {
        'foods': foods,
        'last_two_foods': last_two_foods
    }

# Call the function and print the result
print('Exercise 3:', slice_foods())

# Exercise 4: Dictionaries and String Formatting
#
# Create a dictionary named home_town containing the keys of city, state, and population.
# Using the home_town dictionary, assign to a variable named home_town_message a string with this format: “I was born in <city>, <state> - population of <population>”

def hometown_info():
    home_town = {
        'city': 'San Francisco',
        'state': 'California',
        'population': 873965
    }
    
    home_town_message = f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}"
    
    return {
        'home_town': home_town,
        'home_town_message': home_town_message
    }

# Call the function and print the result
print('Exercise 4:', hometown_info())

# Exercise 5: Iterating Over Dictionary Items
#
# Define an empty list named home_town_items.
# Use a for loop to iterate over the key: value pairs in the home_town dictionary and append a string with the following format to home_town_items: "<key> = <value>"

def list_home_town_items():
    home_town = {
        'city': 'San Francisco',
        'state': 'California',
        'population': 873965
    }
    
    home_town_items = []
    
    for key, value in home_town.items():
        home_town_items.append(f"{key} = {value}")
    
    return {
        'home_town': home_town,
        'home_town_items': home_town_items
    }

# Call the function and print the result
print('Exercise 5:', list_home_town_items())

# Additional demonstration showing individual variables as requested
print("\n=== Individual Variable Demonstrations ===")

# Exercise 1 variables
result1 = manage_students()
students = result1['students']
first_student = result1['first_student']
last_student = result1['last_student']
print(f"Students list: {students}")
print(f"Second student (first_student): {first_student}")
print(f"Last student: {last_student}")

# Exercise 2 variables
result2 = combine_foods()
foods = result2['foods']
meal = result2['meal']
print(f"\nFoods tuple: {foods}")
print(f"Combined meal: {meal}")

# Exercise 3 variables
result3 = slice_foods()
last_two_foods = result3['last_two_foods']
print(f"\nLast two foods: {last_two_foods}")

# Exercise 4 variables
result4 = hometown_info()
home_town = result4['home_town']
home_town_message = result4['home_town_message']
print(f"\nHome town dictionary: {home_town}")
print(f"Home town message: {home_town_message}")

# Exercise 5 variables
result5 = list_home_town_items()
home_town_items = result5['home_town_items']
print(f"\nHome town items list: {home_town_items}")