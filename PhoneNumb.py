from tkinter import *
import math

Number = "0"

def createInterface():
    global window
    window = Tk()

    

    info = Label(window, text="Enter your Phone Number please", font = ("Arial", 15))
    info.grid(columnspan = 5)

    numberLabel = Label(window, text="0", font = ("Arial", 15))
    numberLabel.grid(columnspan = 5)

    addTwo = Button(window, text="+2", command=lambda calculateMath = calculateMath: calculateMath("+2", numberLabel),
                    height = 3, width = 7, font = ("Arial", 15))
    addTwo.grid(row=5, column = 0, columnspan = 2)

    addThree = Button(window, text="+3", command=lambda calculateMath = calculateMath: calculateMath("+3", numberLabel),
                    height = 3, width = 7, font = ("Arial", 15))
    addThree.grid(row=5, column = 2, columnspan = 2)

    multThree = Button(window, text="*3", command=lambda calculateMath = calculateMath: calculateMath("*3", numberLabel),
                    height = 3, width = 7, font = ("Arial", 15))
    multThree.grid(row=5, column = 4, columnspan = 2)

    divideFive = Button(window, text="/5", command=lambda calculateMath = calculateMath: calculateMath("/5", numberLabel),
                    height = 3, width = 7, font = ("Arial", 15))
    divideFive.grid(row=6, column = 1, columnspan = 2)

    squareRoot = Button(window, text="Root", command=lambda calculateMath = calculateMath: calculateMath("Root", numberLabel),
                    height = 3, width = 7, font = ("Arial", 15))
    squareRoot.grid(row=6, column = 1, columnspan = 2)

    divFive = Button(window, text="/5", command=lambda calculateMath = calculateMath: calculateMath("/5", numberLabel),
                    height = 3, width = 7, font = ("Arial", 15))
    divFive.grid(row=6, column = 3, columnspan = 2)

    timesTwoAndHalf = Button(window, text="*2.5", command=lambda calculateMath = calculateMath: calculateMath("*2.5", numberLabel),
                    height = 3, width = 7, font = ("Arial", 15))
    timesTwoAndHalf.grid(row=6, column = 5, columnspan = 2)

    space = Label(window, height = 3).grid(row=7)

    confirmNumber = Button(window, text="Confirm", command=lambda confirm = confirm: confirm(numberLabel),
                           height = 5, width = 15, font = ("Arial", 15))
    confirmNumber.grid(row = 8, column = 0, columnspan = 4)
    
    window.title("Phone Number")
    window.geometry("500x500")
    window.mainloop()


def calculateMath(operation, place):
    global Number
    if operation == "Root":
        Number = str(math.sqrt(float(Number)))
    else:
        Number = str(eval(Number + operation))

    place.configure(text=Number)

def confirm(place):
    global window
    place.configure(text=str(int(float(Number))))

    goodConf = Label(window ,text = "your phone number has been saved as : " + Number, font = ("Arial", 15))
    goodConf.grid(row = 9, column = 0, columnspan = 4)

createInterface()
