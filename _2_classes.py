# == INSTRUCTIONS ==
#
# In these exercises you will build small classes.
#
# The first ones will be familiar, do them without looking at your previous
# work. The later ones will be more complex.
#
# Here is an example of some exercise instructions and a solution.
#
# Class name: ExampleGreeter
# Purpose: say hello and goodbye to a user with a given name
# Methods:
#   1. Name: __init__
#      Arguments: one, a string representing a name
#   2. Name: say_hello
#      Arguments: none
#      Returns: a string like 'Hello, NAME!'
#   3. Name: say_goodbye
#      Arguments: none
#      Returns: a string like 'Goodbye, NAME!'
# Example usage:
#   > greeter = ExampleGreeter('Bobby')
#   > greeter.say_hello()
#   'Hello, Bobby!'
#   > greeter.say_goodbye()
#   'Goodbye, Bobby!'
#
# Example solution:
# class ExampleGreeter():
#     def __init__(self, name):
#         self.name = name
#     def say_hello(self):
#         return 'Hello, ' + self.name + '!'
#     def say_goodbye(self):
#         return 'Goodbye, ' + self.name + '!'
        


# == EXERCISES ==

# Class name: Greeter
# Purpose: say various greetings to a user with a given name
# Methods:
#   1. Name: hello
#      Arguments: one, a string representing a name
#      Returns: a string like 'Hello, NAME!'
#   2. Name: goodbye
#      Arguments: one, a string representing a name
#      Returns: a string like 'Goodbye, NAME!'
#   3. Name: good_night
#      Arguments: one, a string representing a name
#      Returns: a string like 'Good night, NAME!'
#   4. Name: good_morning
#      Arguments: one, a string representing a name
#      Returns: a string like 'Good morning, NAME!'
# Example usage:
#   > greeter = Greeter()
#   > greeter.hello('Bobby')
#   'Hello, Bobby!'
#   > greeter.goodbye('Bobby')
#   'Goodbye, Bobby!'
#   > greeter.good_night('Bobby')
#   'Good night, Bobby!'
#   > greeter.good_morning('Bobby')
#   'Good morning, Bobby!'

class Greeter:
    def __init__(self):
        pass

    def hello(self, name):
        return f'Hello, {name}!'

    def goodbye(self, name):
        return f'Goodbye, {name}!'
        
    def good_night(self, name):
        return f'Good night, {name}!'

    def good_morning(self, name):
        return f'Good morning, {name}!'

    
greeter = Greeter()
print(greeter.hello('Bobby'))
print(greeter.goodbye('Bobby'))
print(greeter.good_night('Bobby'))  
print(greeter.good_morning('Bobby')) 



# Class name: Basket
# Purpose: store a list of items
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Arguments: one item of any type
#      Returns: nothing
#   3. Name: list_items
#      Arguments: none
#      Returns: a list of all the items that have been added
# Example usage:
#   > basket = Basket()
#   > basket.add('apple')
#   > basket.add('banana')
#   > basket.add('orange')
#   > basket.list_items()
#   ['apple', 'banana', 'orange']
class Basket:
    def __init__(self):
        self.basket = []

    def add(self, any_item):
        self.any_item = any_item
        return self.basket.append(any_item)
    
    def list_items(self):
        return (self.basket)
    
basket = Basket()
basket.add('apple')
basket.add('banana')
basket.add('orange')
print(basket.list_items())



# Class name: Calculator
# Purpose: perform simple calculations and track the history
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Arguments: two numbers
#      Returns: the result of adding the two numbers
#   3. Name: multiply
#      Arguments: two numbers
#      Returns: the result of multiplying the first by the second
#   4. Name: subtract
#      Arguments: two numbers
#      Returns: the result of subtracting the second from the first
#   5. Name: divide
#      Arguments: two numbers
#      Returns: the result of dividing the first by the second
#   6. Name: list_history
#      Arguments: none
#      Returns: a list of all the previous results calculations
# Example usage:
#   > calculator = Calculator()
#   > calculator.add(1, 2)
#   3
#   > calculator.multiply(3, 4)
#   12
#   > calculator.subtract(5, 6)
#   -1
#   > calculator.divide(7, 8)
#   0.875
#   > calculator.list_history()
#   [3, 12, -1, 0.875]
class Calculator:
    def __init__(self):
        self.history = []
        
    def add(self, num1, num2):
        result = num1 + num2
        self.history.append(result)
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.history.append(result)
        return result
    
    def substract(self, num1, num2):
        result = num1 - num2
        self.history.append(result)
        return result
    
    def devide(self, num1, num2):
        result = num1 / num2
        self.history.append(result)
        return result
    
    def list_history(self):
        return self.history

calculator = Calculator()
print(calculator.add(1, 2))
print(calculator.multiply(3, 4))
print(calculator.substract(5, 6))
print(calculator.devide(7, 8))
print(calculator.list_history())


# Class name: Cohort
# Purpose: store a list of students
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add_student
#      Arguments: one dictionary representing a student
#      Returns: nothing
#   3. Name: list_students
#      Arguments: none
#      Returns: a list of all the students that have been added
#   4. Name: list_employed_by
#      Arguments: one string, the name of an employer
#      Returns: a list of all the students who work for that employer
# Example usage:
#   > cohort = Cohort()
#   > cohort.add_student({'name' : 'Jo', 'employer' : 'NASA'})
#   > cohort.add_student({'name' : 'Alex', 'employer' : 'NASA'})
#   > cohort.add_student({'name' : 'Bobby', 'employer' : 'Google'})
#   > cohort.list_students()
#   [{'name' : 'Jo', 'employer' : 'NASA'}, {'name' : 'Alex', 'employer' : 'NASA'}, {'name' : 'Bobby', 'employer' : 'Google'}]
#   > cohort.list_employed_by('NASA')
#   [{'name' : 'Jo', 'employer' : 'NASA'}, {'name' : 'Alex', 'employer' : 'NASA'}]
class Cohort:
    def __init__(self):
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)  

    def list_students(self):  
        return self.students 
    
    def list_employed_by(self, employer):
        employed_students = []
        for student in self.students:
            if student["employer"] == employer:  
                employed_students.append(student)
        return employed_students  

# Testing the class
cohort = Cohort()
cohort.add_student({'name' : 'Jo', 'employer' : 'NASA'})
cohort.add_student({'name' : 'Alex', 'employer' : 'NASA'})
cohort.add_student({'name' : 'Bobby', 'employer' : 'Google'})
print(cohort.list_students())
print(cohort.list_employed_by('NASA'))



# Class name: Person
# Purpose: store a person's name, pets and addresses
# Methods:
#   1. Name: __init__
#      Arguments: one complex dictionary, see below for structure.
#   2. Name: get_work_address
#      Arguments: none
#      Returns: the work address in a nice format
#   3. Name: get_home_address
#      Arguments: none
#      Returns: the home address in a nice format
#   4. Name: get_pets
#      Arguments: none
#      Returns: a nice summary of the person's pets
# Example usage:
#   > person = Person({
#       'name' : 'Alex',
#       'pets' : [
#         {'name' : 'Arthur', 'animal' : 'cat'},
#         {'name' : 'Judith', 'animal' : 'dog'},
#         {'name' : 'Gwen', 'animal' : 'goldfish'}
#       ],
#       'addresses' : [
#         {'name' : 'work', 'building' : '50', 'street' : 'Commercial Street'},
#         {'name' : 'home', 'building' : '10', 'street' : 'South Street'}
#       ]
#     })
#   > person.get_work_address()
#   '50 Commercial Street'
#   > person.get_home_address()
#   '10 South Street'
#   > person.get_pets()
#   'Alex has 3 pets: a cat called Arthur, a dog called Judith, a goldfish called Gwen'
class Person:
    def __init__(self, info):
        self.name = info['name']
        self.pets = info['pets']
        self.addresses = info['addresses']

    def get_work_address(self):
        for address in self.addresses:
            if address['name'] == 'work':
                return f"{address['building']} {address['street']}"
        return "Work address not found."

    def get_home_address(self):
        for address in self.addresses:
            if address['name'] == 'home':
                return f"{address['building']} {address['street']}"
        return "Home address not found."

    def get_pets(self):
        pet_descriptions = [f"a {pet['animal']} called {pet['name']}" for pet in self.pets]
        pet_list = ', '.join(pet_descriptions)
        return f"{self.name} has {len(self.pets)} pets: {pet_list}"

# Testing the class
person_info = {
    'name': 'Alex',
    'pets': [
        {'name': 'Arthur', 'animal': 'cat'},
        {'name': 'Judith', 'animal': 'dog'},
        {'name': 'Gwen', 'animal': 'goldfish'}
    ],
    'addresses': [
        {'name': 'work', 'building': '50', 'street': 'Commercial Street'},
        {'name': 'home', 'building': '10', 'street': 'South Street'}
    ]
}

person = Person(person_info)
print(person.get_work_address())  
print(person.get_home_address()) 
print(person.get_pets())  


