# Exercise 0: Example

def example_list_function():
  example_list = ['element1', 'element2', 'element3']
  for element in example_list:
      print(element)

# Call the function and print each element
example_list_function()


# Exercise 1: List and Indexing

def manage_students():
   student_list = ['Mahmood','Aqeel','Husain']

   first_student = student_list[1]
    
   last_student = student_list[-1]
   
   return first_student, last_student

# Call the function and print the result
print('Exercise 1:', manage_students())


# Exercise 2: Loop and String Concatenation

def combine_foods():
    students = ['Mahmood', 'Aqeel', 'Husain']
    foods = ['Pizza', 'Burger', 'Pasta']  # Same number of foods as students
    meal = ''
    
    # Loop through the foods tuple and concatenate each item to meal
    for food in foods:
        meal += food + " "
    
    return meal.strip()  # Removing the extra space at the end


# Exercise 3: Slicing Tuples

# Call the function and print the result
print('Exercise 2:', combine_foods())


def slice_foods():
    foods = ('Pizza', 'Burger', 'Shawarma', 'Machboos', 'Ma3soob')  # Example tuple
    last_two_foods = foods[-2:]  # Slice to get the last two items
    
    return last_two_foods

# Call the function and print the result
print('Exercise 3:', slice_foods())


def hometown_info():
    # Creating the dictionary with keys of my city, state, and population
    home_town = {
        'city': 'Um Al Hassam',
        'state': 'Manama',
        'population': 200000
    }
    
    # Using string formatting to create the message
    home_town_message = f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}"
    
    return home_town_message

# Calling the function and print the result
print('Exercise 4:', hometown_info())


def list_home_town_items():
    # Creating the dictionary with keys city, state, and population
    home_town = {
        'city': 'Um Al Hassam',
        'state': 'Manama',
        'population': 200000
    }
    
    # Defining an empty list to store the formatted strings
    home_town_items = []
    
    # Iterating over key:value pairs and appending formatted strings to the list
    for key, value in home_town.items():
        home_town_items.append(f"{key} = {value}")
    
    return home_town_items

# Call the function and print the result
print('Exercise 5:', list_home_town_items())
