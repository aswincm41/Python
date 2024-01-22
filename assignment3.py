#qs1

# def check_even_odd(number):
#     if number % 2 == 0:
#         print(f"{number} is an even number.")
#     else:
#         print(f"{number} is an odd number.")

# user_input = int(input("Enter an integer: "))
# check_even_odd(user_input)

#qs2

# def create_square_dictionary():
#     square_dict = {num: num**2 for num in range(1, 21)}
#     return square_dict

# result_dict = create_square_dictionary()

# for key, value in result_dict.items():
#     print(f"{key}: {value}")


#qs3


# def remove_vowels(input_string):
#     vowels = "aeiouAEIOU"
#     result_string = ''.join([char for char in input_string if char not in vowels])
#     return result_string
# user_input = input("Enter a string: ")
# result = remove_vowels(user_input)
# print("String with vowels removed:", result)

#qs4

# n = 10 
# powers_of_2 = map(lambda x: 2**x, range(n))
# print("Powers of 2:")
# for power in powers_of_2:
#     print(power)


#qs7
    
   
# def create_dictionary(keys, values):
#     if len(keys) != len(values):
#         print("Error: The input lists must be of the same length.")
#         return None
    
#     result_dict = dict(zip(keys, values))
#     return result_dict
# keys_list = input("Enter keys separated by space: ").split()
# values_list = input("Enter values separated by space: ").split()
# result_dict = create_dictionary(keys_list, values_list)
# if result_dict:
#     print("Resulting Dictionary:", result_dict)


#qs8

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# result = fibonacci(6)
# print("Fibonacci number at position 6 is:", result)



#qs9

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# result = factorial(5)
# print("Factorial of 5 is:", result)


#qs10


