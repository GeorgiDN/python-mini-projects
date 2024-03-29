from tkinter import *
from math import sqrt


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + number)


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)


def button_exponentiation():
    first_number = e.get()
    global f_num
    global math
    math = "exponentiation"
    f_num = float(first_number)
    e.delete(0, END)


def button_square_root():
    first_number = e.get()
    global f_num
    global math
    math = "square_root"
    f_num = float(first_number)
    e.delete(0, END)


def button_percent():
    first_number = e.get()
    global f_num
    global math
    math = "percent"
    f_num = float(first_number)
    e.delete(0, END)


def button_point():
    current = e.get()
    # Check if there is already a decimal point in the current entry
    if '.' not in current:
        e.delete(0, END)
        e.insert(0, current + '.')


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        result = f_num + float(second_number)
    elif math == "subtraction":
        result = f_num - float(second_number)
    elif math == "multiplication":
        result = f_num * float(second_number)
    elif math == "division":
        result = f_num / float(second_number)
    elif math == "exponentiation":
        result = f_num ** float(second_number)
    elif math == "square_root":
        result = sqrt(f_num)
    elif math == "percent":
        result = (f_num * float(second_number)) / 100

    if result % 1 == 0:
        result = int(result)

    e.insert(0, result)

    # Store the calculation in a text file
    if math != "square_root":
        with open('../calculations.txt', 'a') as file:
            file.write(f"{f_num} {math} {second_number} = {result}\n")
    else:
        with open('../calculations.txt', 'a') as file:
            file.write(f"{math} of {f_num}  is {result}\n")


root = Tk()
root.title("My calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

button_1 = Button(root, text='1', padx=40, pady=20, bg="grey", command=lambda: button_click("1"))
button_2 = Button(root, text='2', padx=40, pady=20, bg="grey", command=lambda: button_click("2"))
button_3 = Button(root, text='3', padx=40, pady=20, bg="grey", command=lambda: button_click("3"))
button_4 = Button(root, text='4', padx=40, pady=20, bg="grey", command=lambda: button_click("4"))
button_5 = Button(root, text='5', padx=40, pady=20, bg="grey", command=lambda: button_click("5"))
button_6 = Button(root, text='6', padx=40, pady=20, bg="grey", command=lambda: button_click("6"))
button_7 = Button(root, text='7', padx=40, pady=20, bg="grey", command=lambda: button_click("7"))
button_8 = Button(root, text='8', padx=40, pady=20, bg="grey", command=lambda: button_click("8"))
button_9 = Button(root, text='9', padx=40, pady=20, bg="grey", command=lambda: button_click("9"))
button_0 = Button(root, text='0', padx=40, pady=20, bg="grey", command=lambda: button_click("0"))
button_point = Button(root, text='.', padx=40, pady=20, bg="grey", command=button_point)

button_add = Button(root, text='+', padx=39, pady=20, bg="grey", command=button_add)
button_equal = Button(root, text='=', padx=92, pady=20, bg="blue", command=button_equal)
button_clear = Button(root, text='C', padx=40, pady=20, bg="green", command=button_clear)

button_subtract = Button(root, text='-', padx=41, pady=20, bg="grey", command=button_subtract)
button_multiply = Button(root, text='*', padx=40, pady=20, bg="grey", command=button_multiply)
button_divide = Button(root, text='/', padx=41, pady=20, bg="grey", command=button_divide)
button_exponentiation = Button(root, text='**', padx=38, pady=20, bg="grey", command=button_exponentiation)
button_square_root = Button(root, text='√', padx=38, pady=20, bg="grey", command=button_square_root)
button_percent = Button(root, text='%', padx=38, pady=20, bg="grey", command=button_percent)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_point.grid(row=4, column=1)
button_add.grid(row=4, column=2)

button_subtract.grid(row=5, column=2)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=5, column=0)

button_exponentiation.grid(row=7, column=0)
button_square_root.grid(row=5, column=1)
button_percent.grid(row=6, column=0)

button_clear.grid(row=6, column=2)
button_equal.grid(row=7, column=1, columnspan=2)

root.mainloop()






# from tkinter import *
# from math import sqrt


# def button_click(number):
#     current = e.get()
#     e.delete(0, END)
#     e.insert(0, str(current) + number)
#     return


# def button_clear():
#     e.delete(0, END)


# def button_add():
#     first_number = e.get()
#     global f_num
#     global math
#     math = "addition"
#     f_num = int(first_number)
#     e.delete(0, END)
#     return


# def button_subtract():
#     first_number = e.get()
#     global f_num
#     global math
#     math = "subtraction"
#     f_num = int(first_number)
#     e.delete(0, END)
#     return


# def button_multiply():
#     first_number = e.get()
#     global f_num
#     global math
#     math = "multiplication"
#     f_num = int(first_number)
#     e.delete(0, END)
#     return


# def button_divide():
#     first_number = e.get()
#     global f_num
#     global math
#     math = "division"
#     f_num = int(first_number)
#     e.delete(0, END)
#     return


# def button_exponentiation():
#     first_number = e.get()
#     global f_num
#     global math
#     math = "exponentiation"
#     f_num = int(first_number)
#     e.delete(0, END)


# def button_square_root():
#     first_number = e.get()
#     global f_num
#     global math
#     math = "square_root"
#     f_num = int(first_number)
#     e.delete(0, END)


# def button_percent():
#     first_number = e.get()
#     global f_num
#     global math
#     math = "percent"
#     f_num = int(first_number)
#     e.delete(0, END)


# def button_equal():
#     second_number = e.get()
#     e.delete(0, END)

#     if math == "addition":
#         result = f_num + int(second_number)
#     elif math == "subtraction":
#         result = f_num - int(second_number)
#     elif math == "multiplication":
#         result = f_num * int(second_number)
#     elif math == "division":
#         result = f_num / int(second_number)
#     elif math == "exponentiation":
#         result = f_num ** int(second_number)
#     elif math == "square_root":
#         result = sqrt(f_num)
#     elif math == "percent":
#         result = (f_num * int(second_number)) / 100

#     e.insert(0, result)

#     # Store the calculation in a text file
#     if math != "square_root":
#         with open('calculations.txt', 'a') as file:
#             file.write(f"{f_num} {math} {second_number} = {result}\n")
#     else:
#         with open('calculations.txt', 'a') as file:
#             file.write(f"{math} of {f_num}  is {result}\n")


# root = Tk()
# root.title("My calculator")

# e = Entry(root, width=35, borderwidth=5)
# e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click("1"))
# button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click("2"))
# button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click("3"))
# button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click("4"))
# button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click("5"))
# button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click("6"))
# button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click("7"))
# button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click("8"))
# button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click("9"))
# button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click("0"))
# button_add = Button(root, text='+', padx=39, pady=20, command=button_add)
# button_equal = Button(root, text='=', padx=91, pady=20, command=button_equal)
# button_clear = Button(root, text='Clear', padx=79, pady=20, command=button_clear)

# button_subtract = Button(root, text='-', padx=41, pady=20, command=button_subtract)
# button_multiply = Button(root, text='*', padx=40, pady=20, command=button_multiply)
# button_divide = Button(root, text='/', padx=41, pady=20, command=button_divide)
# button_exponentiation = Button(root, text='**', padx=38, pady=20, command=button_exponentiation)
# button_square_root = Button(root, text='√', padx=38, pady=20, command=button_square_root)
# button_percent = Button(root, text='%', padx=38, pady=20, command=button_percent)

# button_1.grid(row=3, column=0)
# button_2.grid(row=3, column=1)
# button_3.grid(row=3, column=2)

# button_4.grid(row=2, column=0)
# button_5.grid(row=2, column=1)
# button_6.grid(row=2, column=2)

# button_7.grid(row=1, column=0)
# button_8.grid(row=1, column=1)
# button_9.grid(row=1, column=2)

# button_0.grid(row=4, column=0)
# button_add.grid(row=5, column=0)


# button_subtract.grid(row=6, column=0)
# button_multiply.grid(row=4, column=1)
# button_divide.grid(row=4, column=2)

# button_exponentiation.grid(row=7, column=0)
# button_square_root.grid(row=5, column=1)
# button_percent.grid(row=5, column=2)

# button_clear.grid(row=6, column=1, columnspan=2)
# button_equal.grid(row=7, column=1, columnspan=2)
# root.mainloop()
