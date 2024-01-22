# dict={'name':'aswin','age':23,'city':'kollam'}
# print(dict['name'])
# print(dict['age'])
# print(dict['city'])

# dict['occupation']='Engineer'
# dict['city']='pathanapuram'
# dict['age']='25'
# print(dict['occupation'])
# print(dict['city'])
# print(dict['age'])

# remove_value=dict.pop('age')


# keys=dict.keys()
# values=dict.values()
# items=dict.items()
# print('key are',keys)
# print('values are',values)
# print('items are',items)




# if 'age' in dict:
#     print("age exists in the dictionary.")

#accessing,add/modifying,removing, checking

# dict1 = {'a': 1, 'b': 3}
# dict2 = {'b': 2, 'c': 4}

# dict1.update(dict2)
# print(dict1)

# concatenated_dict = {**dict1, **dict2}
# print(concatenated_dict)


squared_numbers = {x: x**2 for x in range(5)}
print(squared_numbers)

even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)

# Dictionary Comprehensive



dict={'name':'aswin','age':23,'city':'kollam'}


age=dict.get('age')
print(age)
# get function

additional_info = {'gender': 'Male', 'education': 'Degree'}
dict.update(additional_info)
print(dict)
# update function

dict.clear()
print(dict)

# clear function