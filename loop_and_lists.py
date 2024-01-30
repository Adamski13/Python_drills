#Exercise 1: Basic List Operations
#Create a list of five numbers.
#Write a loop to iterate through the list and print each number.
numbers = [4,5,6,7,8]
for i in numbers:
    print(i)


#Exercise 2: Advanced List Comprehension
#Given a list of numbers, [1, 2, 3, 4, 5], use a list comprehension to create a new list containing the squares of each number.
numbers = [1, 2, 3, 4, 5]
numbers_squared = [i ** 2 for i in numbers]
print(numbers_squared)
                   

#Exercise 3: Dictionary Basics
#Create a dictionary representing a person, with keys like 'name', 'age', and 'city'. Fill it with some sample data.
#Write a loop to iterate through the dictionary and print each key-value pair.
person = {
    'name': 'Carlos',
    'age': '38',
    'city': 'Toronto',
    }
for item in person.items():
    print(item)

#Exercise 4: Dictionary and List Combination
#Create a list of dictionaries, where each dictionary represents a different person, with keys for 'name' and 'age'.
#Write a loop to iterate through the list and print the name and age of each person.
people = [{'Name':'Adam', 'age':'29'} , {'Name':'Erik', 'age':'50'}, {'Name':'Marco', 'age':'13'}]

for person in people:
    print(f"Name: {person['Name']}, Age: {person['age']}")


#Exercise 5: Nested Loops with Lists
#Create a list of lists, where each inner list contains numbers (e.g., [[1, 2, 3], [4, 5, 6], [7, 8, 9]]).
#Write a nested loop to print each number in each inner list.
lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for inner_list in lists:
    for i in list:
        print(i)
            

#Exercise 6: Dictionary Values and Loops
#Given a dictionary with keys as names and values as ages, write a loop to print the name of each person who is older than 20.
people = {'Adam': 29, 'Erik': 50, 'Marco': 13}
for name, age in people.items():
    if age > 20:
        print(name)


#or above could be done using list of dictionaries
#people = [{'name': 'Adam', 'age': 29}, {'name': 'Erik', 'age': 50}, {'name': 'Marco', 'age': 13}]
#for person in people:
#    if person['age'] > 20:
#        print(person['name'])


#Exercise 7: Complex Data Structures
#Create a dictionary where each key is a username and the value is a list of numbers (e.g., 'user1': [1, 2, 3]).
#Write a loop to iterate through the dictionary and a nested loop to print each number in the user's list."""
user_data = {'user1': [1, 2, 3], 'user2': [5, 6, 8], 'user3': [9, 10, 16]}
for user, numbers in user_data.items():
    for num in numbers:
        print(f"{user}: {num}")


# Exercise 8: List Filtering
# Create a list of numbers.
# Write a loop to create a new list that contains only the even numbers from the original list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)

#another way:
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#even_numbers = [num for num in numbers if num % 2 == 0]
#print(even_numbers)


# Exercise 9: Dictionary Key Manipulation
# Given a dictionary, write a loop to create a new dictionary where the keys are the original keys concatenated with the string "_new".
my_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'mango': 5}
new_dict = {}
for key in my_dict.keys():
   new_key = key + '_new'
   new_dict[new_key] = my_dict[key]
print(new_dict)
    


# Exercise 10: List of Dictionaries Sorting
# Create a list of dictionaries, where each dictionary contains keys like 'name' and 'score'.
# Write code to sort this list of dictionaries by 'score' in descending order.
student_score = [{'name': 'Adam', 'score': 89}, {'name': 'Chiara', 'score': 95}, {'name': 'Helena', 'score': 75}, {'name': 'Alejandro', 'score': 65}]
sorted_score = sorted(student_score, key=lambda item: item['score'], reverse=True)
print(sorted_score)


# Exercise 11: Counting with Dictionaries
# Given a list of strings (e.g., names), use a dictionary to count how many times each string appears in the list.
names = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]

name_count = {}
for name in names:
    if name in name_count:
        name_count[name] += 1
    else:
        name_count[name] = 1

print(name_count)


# Exercise 12: Nested Dictionary Operations
# Create a nested dictionary where each key is a username and the value is another dictionary with keys like 'age' and 'email'.
# Write a loop to print each username and their email.
users = {
    'john_doe': {'age': 30, 'email': 'john@example.com'},
    'jane_smith': {'age': 25, 'email': 'jane@example.com'}
}

for username, user_info in users.items():
    print(f"Username: {username}, Email: {user_info['email']}")


# Exercise 13: Dictionary Values Summation
# Given a dictionary with numeric values, write a loop to calculate the sum of all the values in the dictionary.
my_dict = {'a': 10, 'b': 20, 'c': 30}

total = sum(my_dict.values())

print(f"Total sum: {total}")


# Exercise 14: Complex Data Structure Iteration
# Create a list where each element is a dictionary. Each dictionary should have a key 'data' whose value is a list of numbers.
# Write a loop to print the sum of the numbers in each 'data' list.
data_list = [
    {'data': [1, 2, 3]},
    {'data': [4, 5, 6]},
    {'data': [7, 8, 9]}
]

for item in data_list:
    data_sum = sum(item['data'])
    print(f"Sum of the list {item['data']}: {data_sum}")
