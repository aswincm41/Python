######To Read#####
# file=open('sample.txt',"r")
# x=file.read()
# file.close()

# ######TO Write######

# file = open('sample.txt', 'w')
# file.write("Hello\n")
# file.close()



# #######To Append###
# file=open('sample.txt','a')
# file.write('Hi')
# file.close()

# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)

# with open('example.txt', 'r') as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line)



# with open('sample.txt', 'r') as file:
#     line1 = file.readline()
#     line2 = file.readline()
#     line3 = file.readline()
# print(line1)
# print(line2)


# with open('example.txt', 'w') as file:
#     file.write('Hello, I am Aswin.\n')
#     file.write('This is another line.\n')

# with open('sample.txt','r')as file:
#     content=file.read()
#     print(content)


# import zipfile
# print('Started........')
# zip_file = zipfile.ZipFile('FileZip.zip', 'w')
# zip_file.write('text1.txt', compress_type=zipfile.ZIP_DEFLATED)
# zip_file.write('text2.txt', compress_type=zipfile.ZIP_DEFLATED)
# zip_file.close()

# import zipfile

# print('unZip.....')

# unzip_file = zipfile.ZipFile('FileZip.zip', 'r')

# unzip_file.extractall('Files')

# unzip_file.close()

#######CSV#######
# import csv

# with open('apple.csv', 'r', newline='') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


import csv
with open('apple.csv','a',newline='')as file:
    writer=csv.writer(file)
    tup=("aswin",23)
    writer.writerow(tup)
    print("Data has been appended to 'apple.csv'.")