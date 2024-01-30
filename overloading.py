def add(x, y):
    return x + y

def add(s1, s2):
    return s1 + s2

result1 = add(2, 3)
result2 = add("Hello", " World")

print(result1) 
print(result2)


class Main:
    def sum(farg, *args):
        s = 0
        for element in args:
            s += element
        print('Sum of {0} elements: '.format(len(args)), s)


from threading import Thread

class A(Thread):
    def run(self):
        for i in range(5):
            print("Starting.......")

class B(Thread):
    def run(self):
        for i in range(5):
            print("Stoping...")

# Creating instances of the A and B classes
t1 = A()
t2 = B()

# Starting the threads
t1.start()
t2.start()
