# try:
#     a=0
#     b=0
#     result=a/b
#     print(result)
# except ZeroDivisionError:
#     print("Division by zero error occured")
# except Exception as e:
#     print(f"An unexpect error occurred: {e}")

# try:
#     num=int(input("enter a number:"))
#     assert num%2==0
# except:
#     print("Not an even number!")
# else:
#     reciprocal=1/num
#     print(reciprocal)


try:
    numerator=10
    denominator=0
    result=numerator/denominator
    print(result)
except:
    print("Error:Denominator cannot be 0.")
finally:
    print("this is finally block.")
