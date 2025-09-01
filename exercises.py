
## Exercise 0: Example


def example_list_function():
  example_list = ['element1', 'element2', 'element3']
  for element in example_list:
      print(element)

# Call the function and print each element
example_list_function()


## Exercise 1: List and Indexing


def manage_students():
    # your code here
    students = ['Alice', 'Bob', 'Charlie']
    first_student = students[1]
    last_student = students[-1]
    return { 'first_student': first_student, 'last_student': last_student}


# Call the function and print the result
print('Exercise 1:', manage_students())


## Exercise 2: Loop and String Concatenation

def combine_foods():
    # your code here
    foods = ('Pizza ', 'Burger ', 'Salad ')
    meal = ''
    for food in foods:
        meal += food
    return meal


# Call the function and print the result
print('Exercise 2:', combine_foods())


## Exercise 3: Slicing Tuples


def slice_foods():
    # your code here
    foods = ('Pizza', 'Burger', 'Salad')
    last_two_foods = foods[-2:]
    return last_two_foods

# Call the function and print the result
print('Exercise 3:', slice_foods())

## Exercise 4: Dictionaries and String Formatting


def hometown_info():
    # your code here
    home_town = {
        'city': 'Sitra',
        'state': 'Bahrain',
        'population': 2000000
    }
    home_town_message = f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}"
    return home_town_message

# Call the function and print the result
print('Exercise 4:', hometown_info())

## Exercise 5: Iterating Over Dictionary Items


def list_home_town_items():
    # your code here
    home_town = {
        'city': 'Sitra',
        'state': 'Bahrain',
        'population': 2000000
    }
    home_town_items = []
    for key, value in home_town.items():
        home_town_items.append(f"{key} = {value}")
    return home_town_items

# Call the function and print the result
print('Exercise 5:', list_home_town_items())

