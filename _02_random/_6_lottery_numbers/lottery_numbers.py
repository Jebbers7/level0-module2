import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    rand1 = random.randint(0,9)
    rand2 = random.randint(0,9)
    rand3 = random.randint(0,9)
    rand4 = random.randint(0,9)
    rand5 = random.randint(0,9)
    rand6 = random.randint(0,9)
    # TODO 2) Display the selected numbers to the user in a pop-up
    messagebox.showinfo("Lottery Ticket", "Your ticket numbers are: " + str(rand1) + str(rand2) + str(rand3) + str(rand4) + str(rand5) + str(rand6))
    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
