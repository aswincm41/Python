from tkinter import*
window=Tk()
window.title("element")
window.geometry("500x600")
# window.resizable(False,True)
# window.configure(bg='red')
l1=Label(window,text="Hello world")
l1.pack()
e1=Entry(window)
e1.pack()
btn1=Button(window,text='Login')
btn1.pack()
window.mainloop()

#     def show_message(self):
#         user_input = self.entry.get()
#         if user_input:
#             messagebox.showinfo("Message", f"You entered: {user_input}")
#         else:
#             messagebox.showwarning("Warning", "Please enter something!")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = MyTkinterApp(root)
#     root.mainloop()



# from tkinter import *

# # creating root window
# root = Tk()
# root.title("Welcome to Python Lobby")
# # function defined which is called when button is clicked
# def clicked():
#     print("I am clicked")
# # placing Button to our GUI app
# btn = Button(root, text="Click me", command = clicked)
# btn.pack()
# root.geometry('250x200')
# root.mainloop()


# from tkinter import *
# # creating root window
# root = Tk()
# root.title("Welcome to Python Lobby")
# # placing Entry widget to our GUI app
# entry = Entry(root)
# entry.pack()
# root.geometry('250x200')
# root.mainloop()



# from tkinter import *

# root = Tk()
# root.title("PythonLobby")

# w = Label(root, text="Red Zone", bg="red", fg="black")
# w.grid(row=0, column=0)
# w = Label(root, text="Green Glossy", bg="light green", fg="black")
# w.grid(row=1, column=1)
# w = Label(root, text="Yellow", bg="yellow", fg="black")
# w.grid(row=2, column=2)

# root.geometry("250x150")
# root.mainloop()




