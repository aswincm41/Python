def square(x):
    return x**2
a=lambda x:x**2
print(square(5)) 
print(a(5))
   

def square(x):
    return x**2
add=lambda x,y:x+y
print(add(4,5))

#lambda functions


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filter_even = lambda x: x % 2 == 0
even_numbers = list(filter(filter_even, numbers))

print("Original numbers:", numbers)
print("Even numbers:", even_numbers)

#filter function
num = [1,2,3,4,5,6,7,8,9,10]

filter_odd = lambda x:x % 2 == 1
odd_numbers = list(filter(filter_odd, numbers))

print("Original numbers:", numbers)
print("odd numbers:", odd_numbers)

def filter_long_words(word):
    return len(word) > 3
words = ["apple", "banana", "kiwi", "orange", "grape"]
filtered_words = list(filter(filter_long_words, words))
print("Original words:", words)
print("Words longer than 3 characters:", filtered_words)

#filter function

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
result_list = list(squared_numbers)
print("Original numbers:", numbers)
print("Squared numbers:", result_list)


#map function
Double = lambda x: x * 2
numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(Double, numbers)
result_list = list(doubled_numbers)
print("Original numbers:", numbers)
print("Doubled numbers:", result_list)

#double

names = ["John", "Alice", "Bob"]
ages = [25, 30, 22]
zipped_data = zip(names, ages)
result_list = list(zipped_data)
print("Names:", names)
print("Ages:", ages)
print("Zipped data:", result_list)

#zip function