from threading import Thread

class A(Thread):
    def run(self):
        for i in range(3):
            print("Starting.......")

class B(Thread):
    def run(self):
        for i in range(5):
            print("Stoping.....")
class C(Thread):
    def run(self):
        for i in range(5):
            print("Loading........")
t1 = A()
t2 = B()
t3 = C()


t1.start()
t2.start()
t3.start()