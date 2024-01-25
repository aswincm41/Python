######To Read#####
file=open('sample.txt',"r")
x=file.read()
file.close()

# ######TO Write######

file = open('sample.txt', 'w')
file.write("Hello\n")
file.close()



# #######To Append###
file=open('sample.txt','a')
file.write('Hi')
file.close()