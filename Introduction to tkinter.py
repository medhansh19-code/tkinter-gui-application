import tkinter as tk
# Import tkinter library.
# tkinter is used to create GUI (Graphical User Interface) applications in Python.
# "tk" is a short name (alias) that we use to write tkinter more easily.

root=tk.Tk()
# Tk() is a method that creates a new window or the main window of our application.
# "root" is the variable that stores this window.

root.title('Introduction to tkinter')
# title() is a method in the tkinter library that sets the title of the window.
# The text 'Introduction to tkinter' will be displayed in the title bar of the window.

root.geometry('500x500')
# geometry() is a method in the tkinter library that sets the size of the window.
# The dimensions are stored in a string format.
# '500x500' means the window will be 500 pixels wide and 500 pixels high.

root.config(bg='blue')
# config() is a method in the tkinter library that is used to configure
# or change the properties of the window.
# "bg" stands for background.
# bg='blue' changes the background colour of the window to blue.

label=tk.Label(root,text='Click the Button!')
# Label() is a method in the tkinter library that creates a label.
# A label is used to display text or information on the window.
# "root" tells tkinter that the label will be placed inside the main window.
# text='Click the Button!' sets the text that will be displayed on the label.
# "label" is the variable that stores this label.

label.place(x=190,y=100)
# place() is a method in tkinter that is used to position the label.
# x=190 means the label will be placed 190 pixels from the left side.
# y=100 means the label will be placed 100 pixels from the top of the window.
# This position keeps the label approximately in the center.

button=tk.Button(root,text='Greet!',bg='red')
# Button() is a method in the tkinter library that creates a button.
# A button is used to allow the user to perform an action by clicking it.
# "root" tells tkinter that the button will be placed inside the main window.
# text='Greet!' sets the text that will be displayed on the button.
# bg='red' changes the background colour of the button to red.
# "button" is the variable that stores this button.

button.place(x=220,y=200)
# place() is a method in tkinter that is used to position the button.
# x=220 means the button will be placed 220 pixels from the left side.
# y=200 means the button will be placed 200 pixels from the top of the window.
# This places the button below the label with some space between them.

entry=tk.Entry(root)
# Entry() is a method in the tkinter library that creates an entry box.
# An entry box is used to allow the user to enter or type text.
# "root" tells tkinter that the entry box will be placed inside the main window.
# "entry" is the variable that stores this entry box.

entry.place(x=190,y=300)
# place() is a method in tkinter that is used to position the entry box.
# x=190 means the entry box will be placed 190 pixels from the left side.
# y=300 means the entry box will be placed 300 pixels from the top of the window.
# This places the entry box below the button with some space between them.

root.mainloop()
# mainloop() is a method in the tkinter library that starts the event loop.
# It keeps the window open and running.
# It waits for the user to interact with the window, such as clicking, typing or closing it.
# Without mainloop(), the window would open and immediately close.