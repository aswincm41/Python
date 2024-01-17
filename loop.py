# fruits=["orange","apple","cherry"]
# for fruit in fruits:
#     print(fruit)

# names=["aswin","yadhu","pranav"]
# for name in names:
#         if name == "aswin":
#               print(name)

# items=["shoe","shirt","table","shoe"]
# for item in items:
#       if item == "shoe":
#              print(item)

# #for loop

# count=1
# while count <=5:
#     print(f"count is {count}")
#     count +=1

# count=0
# while count<8:
#     print(count)
#     count+=1

# i=1
# while(i<6):
#     print(i)

    #while loop

# for i in range(10):
#     print(i)
#     if i==2:
#         break

  
# i=0
# while i<6:
#     print(i)
#     if i==4:
#         break
#     i+=1

#break

# i=0
# while i<7:
#     i+=1
#     if i==5:
#         continue
#     print(i)
    
#range

# for i in range(10):
#     i+=1
#     if i==5:
#         continue
#     print(i)

# for i in range(5):
#     print(i)
#     print()

#range
    
# for x in  range(3):
#     for i in range(1,5):
#      print(i,end="       ")
#     print()

# #nested loop
    
# for x in range(4):
#     for i in range(x):
#      print("*", end="     ")
#     print()

# i=list (range(1,10,2))
# print(i)

# a=["orange","apple","cherry"]
# i=list(enumerate(a))
# print(i)

# a=["orange","apple","cherry"]
# i=dict(enumerate(a))
# print(i)
# #enumerate(to find the index value)

fruits=["orange","apple","cherry"]
for x,y in enumerate(fruits):
    if(x==2):
        print(x,y)
    else:
        continue