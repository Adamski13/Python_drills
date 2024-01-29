# == INSTRUCTIONS ==
#
# In these exercises you will recap basic dictionary and list operations, then
# go deeper on both topics.
#
# The requirements will always start with the name of the function. Use this
# name exactly or the tests won't be able to find it.
#
# Then there will be a description of what the function should do. Note that
# some solutions will require more than one line of code.
#
# You won't find everything that you need in our materials. Use the Python Docs
# and Google liberally if you get stuck.

# == LIST EXERCISES ==

# Method name: fourth_element
# Purpose: returns the fourth element of the given list
# Arguments: one list
# Example:
#   Call:    fourth_element([1, 2, 3, 4, 5])
#   Returns: 4
def fourth_element(list):
    return list[3]


# Method name: average
# Purpose: returns the average (the mean) of the given list
# Arguments: one list
# Example:
#   Call:    average([3, 1, 44, 1])
#   Returns: 12.25
def average(list):
    return sum(list) / len(list)



# Method name: lowest_squared
# Purpose: returns the lowest number squared
# Arguments: one list
# Example:
#   Call:    lowest_squared([5, 3, 44, 7])
#   Returns: 9
def lowest_squared(list):
    list.sort()
    return list[0] ** 2




# Method name: highest_squared
# Purpose: returns the highest number squared
# Arguments: one list
# Example:
#   Call:    highest_squared([5, 3, 44, 7])
#   Returns: 1936
def highest_squared(list):
    list.sort()
    return list[-1] ** 2



# Method name: starts_with_a
# Purpose: returns only elements starting with 'a'
# Arguments: one list
# Example:
#   Call:    starts_with_a(['banana', 'apple', 'orange', 'avocado'])
#   Returns: ['apple', 'avocado']
def starts_with_a(list):
    new_list = []
    for item in list:
        if item[0] == 'a':
            new_list.append(item)
    return new_list


# Method name: starts_with_a_vowel
# Purpose: returns only the elements that start with a vowel
# Arguments: one list
# Example:
#   Call:    starts_with_a_vowel(['banana', 'apple', 'orange', 'avocado'])
#   Returns: ['apple', 'orange', 'avocado']
def starts_with_a_vowel(list):
    new_list = []
    for item in list:
        if item[0] in 'aeiou':
            new_list.append(item)
    return new_list


# Method name: reverse_each_element
# Purpose: reverses each string in the given list
# Arguments: one list
# Example:
#   Call:    reverse_each_element(['one', 'two'])
#   Returns: ['eno', 'owt']
def reverse_each_element(list):
    reversed_string_list = []
    for string in list:
        reversed_string_list.append(string[::-1])
    return reversed_string_list

print(reverse_each_element(['one', 'two']))

# Method name: sort_by_last_letter
# Purpose: returns the list, sorted by the last letter alphabetically
# Arguments: one list
# Example:
#   Call:    sort_by_last_letter(['banana', 'apple', 'carrot', 'avocado'])
#   Returns: ['banana', 'apple', 'avocado', 'carrot']

#***this one wasnt easy
def sort_by_last_letter(list):
    sorted_list = sorted(list, key=get_last_letter)
    return sorted_list

def get_last_letter(word):
        return word[-1]

print(sort_by_last_letter(['banana', 'apple', 'carrot', 'avocado']))


# Method name: greater_than_5
# Purpose: returns only numbers greater than 5
# Arguments: one list
# Example:
#   Call:    greater_than_5([9, 3, 44, 7])
#   Returns: [9, 44, 7]
def greater_than_5(numbers):
    greater_than_5  = []
    for number in numbers:
        if number > 5:
            greater_than_5.append(number)
    return greater_than_5
    

print(greater_than_5([9, 3, 44, 7]))


# Method name: greater_than
# Purpose: returns only the elements that are greater than the number provided
# Arguments: one list and one number
# Example:
#   Call:    greater_than([9, 3, 6, 44, 7, 7], 6)
#   Returns: [9, 44, 7, 7]
def greater_than(list_numbers, number):
    greater_than = []
    for num in list_numbers:
        if num > number:
            greater_than.append(num)
    return greater_than 

print(greater_than([9, 3, 6, 44, 7, 7], 6))


# Method name: less_than
# Purpose: returns only the elements that are less than the number provided
# Arguments: one list and one number
# Example:
#   Call:    less_than([9, 3, 6, 44, 1, 7, 7], 6)
#   Returns: [3, 1]
def less_than(list_numbers, number):
    less_than = []
    for num in list_numbers:
        if num < number:
            less_than.append(num)
    return less_than   

print(less_than([9, 3, 6, 44, 1, 7, 7], 6))


# Method name: words_shorter_than
# Purpose: returns only the elements that have fewer characters than the number provided
# Arguments: one list and one number
# Example:
#   Call:    words_shorter_than(['banana', 'apple', 'orange', 'nut', 'avocado'], 6)
#   Returns: ['apple', 'nut']
def words_shorter_than(list_words, number):
    shorter_than_num =[]
    for word in list_words:
        if len(word) < 6:
            shorter_than_num.append(word)
    return shorter_than_num

print(words_shorter_than(['banana', 'apple', 'orange', 'nut', 'avocado'], 6))



# Method name: all_above
# Purpose: returns True if all elements are greater than the number provided
# Arguments: one list and one number
# Example:
#   Call:    all_above([9, 3, 6, 44, 1, 7, 7], 6)
#   Returns: False
#   Call:    all_above([9, 3, 6, 44, 1, 7, 7], 0)
#   Returns: True
def all_above(list_numbers, number):
    for num in list_numbers:
        if num <= number:
            return False
        
    return True
    
print(all_above([9, 3, 6, 44, 1, 7, 7], 6))
print(all_above([9, 3, 6, 44, 1, 7, 7], 0))


# Method name: all_below
# Purpose: returns True if all elements are less than the number provided
# Arguments: one list and one number
# Example:
#   Call:    all_below([9, 3, 6, 44, 1, 7, 7], 6)
#   Returns: False
#   Call:    all_below([9, 3, 6, 44, 1, 7, 7], 100)
#   Returns: True
def all_below(list_numbers, number):
    for num in list_numbers:
        if num >= number:
            return False
        
    return True

print(all_below([9, 3, 6, 44, 1, 7, 7], 6))
print(all_below([9, 3, 6, 44, 1, 7, 7], 100))


# Method name: multiply_each_by
# Purpose: returns a new list with each element multiplied by the number provided
# Arguments: one list and one number
# Example:
#   Call:    multiply_each_by([9, 3, 6, 44, 1, 7, 7], 2)
#   Returns: [18, 6, 12, 88, 2, 14, 14]
def multiply_each_by(list_numbers, number):
    multiplied_numbers = []
    for num in list_numbers:
        multiplied_numbers.append(num * number)

    return multiplied_numbers

print(multiply_each_by([9, 3, 6, 44, 1, 7, 7], 2))


# == DICTIONARY EXERCISES ==

# Method name: values_summed
# Purpose: returns the total of all the values in the given dictionary
# Arguments: one dictionary
# Example:
#   Call:    values_summed({'cat': 4, 'person': 2, 'centipede': 100})
#   Returns: 106
def values_summed(dict):
    total = 0
    for value in dict.values():
        total += value
    return total

print(values_summed({'cat': 4, 'person': 2, 'centipede': 100}))


# Method name: add_key_value_pair
# Purpose: returns the dictionary with the new key and value added
# Arguments: one dictionary, one key and one value
# Example:
#   Call:    add_key_value_pair({'cat': 4, 'person': 2, 'centipede': 100}, 'dog', 4)
#   Returns: {'cat': 4, 'person': 2, 'centipede': 100, 'dog': 4}
def add_key_value_pair(dict, key, value):
    dict[key] = value
    return dict
   

print(add_key_value_pair({'cat': 4, 'person': 2, 'centipede': 100}, 'dog', 4))



# Method name: remove_key_value_pair
# Purpose: returns the dictionary with the key and value removed
# Arguments: one dictionary and one key
# Example:
#   Call:    remove_key_value_pair({'cat': 4, 'person': 2, 'centipede': 100}, 'cat')
#   Returns: {'person': 2, 'centipede': 100}
def remove_key_value_pair(dict, key):
    dict.pop(key)
    return dict

print(remove_key_value_pair({'cat': 4, 'person': 2, 'centipede': 100}, 'cat'))



# Method name: where_value_below
# Purpose: returns key value pairs where the value is less than the number provided
# Arguments: one dictionary and one number
# Example:
#   Call:    where_value_below({'cat': 4, 'person': 2, 'centipede': 100}, 5)
#   Returns: {'cat': 4, 'person': 2}

def where_value_below(dict, num):
    new_dict = {}
    for key, value in dict.items():
        if value < num:
           new_dict[key] = value        #"Add a key-value pair to the dict where the key is the same as the key and value from the original dictionary
    return new_dict

print(where_value_below({'cat': 4, 'person': 2, 'centipede': 100}, 5))



# Method name: where_key_starts_with
# Purpose: returns key value pairs where the key starts with the letter provided
# Arguments: one dictionary and one letter
# Example:
#   Call:    where_key_starts_with({'cat': 4, 'person': 2, 'centipede': 100}, 'c')
#   Returns: {'cat': 4, 'centipede': 100}
def where_key_starts_with(dict, letter):
    new_dict = {}
    for key, value in dict.items():
        if key[0] == letter:
           new_dict[key] = value
    return new_dict

print(where_key_starts_with({'cat': 4, 'person': 2, 'centipede': 100}, 'c'))
