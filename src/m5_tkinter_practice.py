"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Jared Brown.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # -------------------------------------------------------------------------
    # DONE: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # -------------------------------------------------------------------------


    root = tkinter.Tk()
    frame1 = ttk.Frame(root, padding=20)
    frame1.grid()
    button1= ttk.Button(frame1, text='Click Me')
    button1['command'] = (lambda: printer())
    button1.grid()

    entry1 = ttk.Entry(frame1)
    button2 = ttk.Button(frame1, text='Click Me')
    button2['command'] = (lambda: printer2(entry1))
    button2.grid()

    entry2 = ttk.Entry(frame1)
    button3 = ttk.Button(frame1, text='Click Me')
    button3['command'] = (lambda: printer3(entry1,entry2))
    button3.grid()

    button1Label = ttk.Label(frame1, text="Hello")
    button2Label = ttk.Label(frame1, text="Hello vs Goodbye")
    button3Label = ttk.Label(frame1, text="Big Thing")
    entry1Label = ttk.Label(frame1, text="Type something")
    entry2Labal= ttk.Label(frame1, text="Type a number here")



    button1Label.grid(row=0,column=0)
    button2Label.grid(row=0,column=2)
    button3Label.grid(row=0,column=4)
    button2Label.grid(row=0,column=2)
    entry1Label.grid(row=1,column=0)
    entry2Labal.grid(row=1,column=3)
    button1.grid(row=0,column=1)
    button2.grid(row=0,column=3)
    button3.grid(row=0,column=5)
    entry1.grid(row=1,column=1)
    entry2.grid(row=1,column=4)



    root.mainloop()

def printer():
    print('Hello')

def printer2(entryBox):
    contents=entryBox.get()
    if(contents=='ok'):
        print('Hello')
    else:
        print('Goodbye')

def printer3(entryBox1,entryBox2):
    for k in range(int(entryBox2.get())):
        print(entryBox1.get())



    # -------------------------------------------------------------------------
    # DONE: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # DONE: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # -------------------------------------------------------------------------


    # -------------------------------------------------------------------------
    # DONE: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # -------------------------------------------------------------------------


    # -------------------------------------------------------------------------
    # DONE: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # DONE: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # -------------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################

    # -------------------------------------------------------------------------
    # TODO: 8. As time permits, do other interesting GUI things!
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
