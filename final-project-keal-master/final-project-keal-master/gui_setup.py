from tkinter import *

# test of function called by button and passed values
def test_func(entry, value):
    print("Testing grabbing from text box:", entry, value)

# test of pop up window
def popup():
    #Window
    root = Tk()

    #Closes popup
    button = Button(root, text="Close", command=root.destroy)
    button.pack()
    from itertools import permutations

    perm = permutations('1234567890', 6)
    count = 0
    f = open("unused919.txt", "w+")
    n = open("test1.txt", "w+")

    for i in set(perm):

        k = ",".join(i)
        k = k.replace(",", "")
        print(k)

        d = dict()
        r = input("Enter your name:")
        if (r == 'q'):
            break
        d[r] = k
        count += 1

        f.write(str(k) + "\n")
        for kp in sorted(d.keys()):
            n.write("'%s':'%s', \n" % (kp, d[kp]))

    f.close()
    n.close()
    
    root.mainloop()

#width and height of window
WIDTH = 500
HEIGHT = 300

# Window
root = Tk()
root.title("919# Generator!")
#Sets v to what the radiobuttons will be
v = IntVar()
v.set(1)

# Sets the options of the window
canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# Square of the window (Can make multiple in future)
frame = Frame(root)
frame.place(relwidth=1, relheight=1)

# Sets label of program
label = Label(frame, text="919# Generator")
label.pack()

# Label before user input
nameLabel = Label(frame, text="Please enter your name")
nameLabel.pack()

# User input (Their name
userName = Entry(frame)
userName.pack()

# First radio button, undergraduate
underGrad = Radiobutton(frame, text="Undergraduate", variable=v, value=1)
underGrad.pack()

# Second radio button, graduate
grad = Radiobutton(frame, text="Graduate", variable=v, value=2)
grad.pack()

# Ok button, currently test to make sure to grab from user input and send it to def
button = Button(frame, text="OK", command=lambda: test_func(userName.get(), v.get()))
button.pack()

# pop up button, currently test to make a pop up window
popbtn = Button(frame, text="pop", command=popup)
popbtn.pack()

# makes sure window does not close before user wants it
root.mainloop()
