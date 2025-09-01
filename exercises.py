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
################################################
# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

# ANS EX.1

def manage_students():
    students = ["Alice", "Bob", "Charlie"]  # list of student names
    first_student = students[1]  # second student
    last_student = students[-1]  # last student
    return first_student, last_student  # return the two variables

# print the result
print('Exercise 1:', manage_students())


################################################
# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.

# ANS EX.2

def combine_foods():
    foods = ("Pizza", "Burger", "Salad")  # all foods
    meal = ""  # start with empty string
    for food in foods:
        meal += food + " "  # add each food to meal with a space
    return meal.strip()  # remove extra space at the end

# print the result
print('Exercise 2:', combine_foods())

################################################

# Exercise 3: Slicing Tuples
#
# Using the slice operator, assign a new tuple containing only the last two food strings in the foods to a variable named last_two_foods.

# ANS EX.3

def slice_foods():
    foods = ("Pizza", "Burger", "Salad")  # tuple of foods
    last_two_foods = foods[-2:]  # slice to get last two items
    return last_two_foods  # return the result

# print the result
print('Exercise 3:', slice_foods())

################################################
# Exercise 4: Dictionaries and String Formatting
#
# Create a dictionary named home_town containing the keys of city, state, and population.
# Using the home_town dictionary, assign to a variable named home_town_message a string with this format: “I was born in <city>, <state> - population of <population>”


# ANS EX.4

def hometown_info():
    home_town = {
        "city": "Manama",
        "state": "Bahrain",
        "population": 200000
    }  # hometown information
    
    home_town_message = "I was born in " + home_town["city"] + ", " + home_town["state"] + " - population of " + str(home_town["population"])
    return home_town_message  # return the message

# print the result
print('Exercise 4:', hometown_info())

################################################
# Exercise 5: Iterating Over Dictionary Items
#
# Define an empty list named home_town_items.
# Use a for loop to iterate over the key: value pairs in the home_town dictionary and append a string with the following format to home_town_items: "<key> = <value>"


# ANS EX.5

def list_home_town_items():
    home_town = {
        "city": "Manama",
        "state": "Bahrain",
        "population": 200000
    }  # same dictionary 
    
    home_town_items = []  # empty list to store the strings
    for key, value in home_town.items():  # loop through each key value pair
        home_town_items.append(key + " = " + str(value))  # add formatted string 
        
    return home_town_items  # return the list

#  print the result
print('Exercise 5:', list_home_town_items())




