#======================#
#  Tkinter Calculator  #
#----------------------#
#  Konstantinos Thanos #
#   Mathematician, MSc #
#======================#

# Import packages
from tkinter import *
import math
import numpy as np

'''
Functions
'''
# Function to add in the entry of text display
def button_click(char):
    global calc_operator
    calc_operator += str(char)
    text_input.set(calc_operator)

# Function to clear the whole entry of text display
def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")

# Function to delete one by one from the last in the entry of text display
def button_delete():
    global calc_operator
    text = calc_operator[:-1]
    calc_operator = text
    text_input.set(text)

# Function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    else:
        return n * factorial(n - 1)

def fact_func():
    global calc_operator
    try:
        val = int(calc_operator)
        if val < 0:
            raise ValueError("Negative factorial")
        result = str(factorial(val))
    except (ValueError, TypeError):
        result = "ERROR"
    calc_operator = result
    text_input.set(result)

# Function to calculate trigonometric numbers of an angle
def trig_sin():
    global calc_operator
    try:
        val = float(calc_operator)
        result = str(math.sin(math.radians(val)))
    except ValueError:
        result = "ERROR"
    calc_operator = result
    text_input.set(result)

def trig_cos():
    global calc_operator
    try:
        val = float(calc_operator)
        result = str(math.cos(math.radians(val)))
    except ValueError:
        result = "ERROR"
    calc_operator = result
    text_input.set(result)

def trig_tan():
    global calc_operator
    try:
        val = float(calc_operator)
        rad = math.radians(val)
        tan_val = math.tan(rad)
        # Avoid extremely large values (near 90 degrees)
        if abs(tan_val) > 1e10:
            raise ValueError("tan undefined")
        result = str(tan_val)
    except (ValueError, ZeroDivisionError):
        result = "ERROR"
    calc_operator = result
    text_input.set(result)

def trig_cot():
    global calc_operator
    try:
        val = float(calc_operator)
        tan_val = math.tan(math.radians(val))
        if tan_val == 0:
            raise ZeroDivisionError
        result = str(1 / tan_val)
    except (ValueError, ZeroDivisionError):
        result = "ERROR"
    calc_operator = result
    text_input.set(result)

# Function to find the square root of a number
def square_root():
    global calc_operator
    try:
        val = float(calc_operator)
        if val < 0:
            raise ValueError("Negative root")
        temp = str(math.sqrt(val))
    except (ValueError, TypeError):
        temp = "ERROR"
    calc_operator = temp
    text_input.set(temp)

# Function to find the third root of a number
def third_root():
    global calc_operator
    try:
        val = float(calc_operator)
        # Cube root is defined for negative numbers as well
        temp = str(val ** (1 / 3))
    except (ValueError, TypeError):
        temp = "ERROR"
    calc_operator = temp
    text_input.set(temp)

# Function to change the sign of number
def sign_change():
    global calc_operator
    if calc_operator:
        if calc_operator[0] == '-':
            temp = calc_operator[1:]
        else:
            temp = '-' + calc_operator
        calc_operator = temp
        text_input.set(temp)

# Function to calculate the percentage of a number
def percent():
    global calc_operator
    try:
        val = float(calc_operator)
        temp = str(val / 100)
    except (ValueError, TypeError):
        temp = "ERROR"
    calc_operator = temp
    text_input.set(temp)

# Function to find e^x
def exp_func():
    global calc_operator
    try:
        val = float(calc_operator)
        temp = str(math.exp(val))
    except (ValueError, TypeError, OverflowError):
        temp = "ERROR"
    calc_operator = temp
    text_input.set(temp)

# Function to evaluate the expression safely
def button_equal():
    global calc_operator
    try:
        # Allowed functions mapping for eval
        allowed_names = {
            'abs': abs,
            'round': round,
            'sin': lambda x: math.sin(math.radians(x)),
            'cos': lambda x: math.cos(math.radians(x)),
            'tan': lambda x: math.tan(math.radians(x)),
            'log': math.log10,
            'ln': math.log,
            'sqrt': math.sqrt,
            'e': math.e,
            'pi': math.pi,
            'pow': pow
        }
        # Replace custom calls to functions to standard Python functions
        expression = calc_operator.replace('log(', 'log(').replace('ln(', 'ln(').replace('abs(', 'abs(')
        # Evaluate safely
        temp_op = eval(expression, {"__builtins__": None}, allowed_names)
        # Convert result to string
        calc_operator = str(temp_op)
        text_input.set(calc_operator)
    except Exception:
        calc_operator = "ERROR"
        text_input.set("ERROR")

'''
Variables
'''
sin, cos, tan = math.sin, math.cos, math.tan
log, ln = math.log10, math.log
e = math.exp
p = math.pi
E = '*10**'

tk_calc = Tk()
tk_calc.configure(bg="#293C4A", bd=10)
tk_calc.title("Scientific Calculator")

calc_operator = ""
text_input = StringVar()

text_display = Entry(tk_calc, font=('sans-serif', 20, 'bold'), textvariable=text_input,
                     bd=5, insertwidth=5, bg='#BBB', justify='right')
text_display.grid(columnspan=5, padx=10, pady=15)

button_params = {'bd':5, 'fg':'#BBB', 'bg':'#3C3636', 'font':('sans-serif', 20, 'bold')}
button_params_main = {'bd':5, 'fg':'#000', 'bg':'#BBB', 'font':('sans-serif', 20, 'bold')}

'''
Buttons
'''
#--1st row--
# Absolute value of a number
abs_value = Button(tk_calc, button_params, text='abs',
                   command=lambda:button_click('abs('))
abs_value.grid(row=1, column=0, sticky="nsew")
# Remainder of a division
modulo = Button(tk_calc, button_params, text='mod',
                command=lambda:button_click('%'))
modulo.grid(row=1, column=1, sticky="nsew")
# Integer division quotient
int_div = Button(tk_calc, button_params, text='div',
                 command=lambda:button_click('//'))
int_div.grid(row=1, column=2, sticky="nsew")
# Factorial of a number
factorial_button = Button(tk_calc, button_params, text='x!',
                   command=fact_func)
factorial_button.grid(row=1, column=3, sticky="nsew")
# Euler's number e
eulers_num = Button(tk_calc, button_params, text='e',
                    command=lambda:button_click(str(math.exp(1))))
eulers_num.grid(row=1, column=4, sticky="nsew")

#--2nd row--
# Sine of an angle in degrees
sine = Button(tk_calc, button_params, text='sin',
             command=trig_sin)
sine.grid(row=2, column=0, sticky="nsew")
# Cosine of an angle in degrees
cosine = Button(tk_calc, button_params, text='cos',
             command=trig_cos)
cosine.grid(row=2, column=1, sticky="nsew")
# Tangent of an angle in degrees
tangent = Button(tk_calc, button_params, text='tan',
             command=trig_tan)
tangent.grid(row=2, column=2, sticky="nsew")
# Cotangent of an angle in degrees
cotangent = Button(tk_calc, button_params, text='cot',
             command=trig_cot)
cotangent.grid(row=2, column=3, sticky="nsew")
# Pi(3.14...) number 
pi_num = Button(tk_calc, button_params, text='π',
                command=lambda:button_click(str(math.pi)))
pi_num.grid(row=2, column=4, sticky="nsew")

#--3rd row--
# Power of 2
second_power = Button(tk_calc, button_params, text='x\u00B2',
             command=lambda:button_click('**2'))
second_power.grid(row=3, column=0, sticky="nsew")
# Power of 3
third_power = Button(tk_calc, button_params, text='x\u00B3',
             command=lambda:button_click('**3'))
third_power.grid(row=3, column=1, sticky="nsew")
# Exponential e^x
exponential = Button(tk_calc, button_params, text='e^x',
             command=exp_func)
exponential.grid(row=3, column=2, sticky="nsew")
# Square root of a number
square_root_btn = Button(tk_calc, button_params, text='\u221A',
             command=square_root)
square_root_btn.grid(row=3, column=3, sticky="nsew")
# Third root of a number
third_root_btn = Button(tk_calc, button_params, text='3\u221B',
             command=third_root)
third_root_btn.grid(row=3, column=4, sticky="nsew")

#--4th row--
# Number 7
seven = Button(tk_calc, button_params_main, text='7',
             command=lambda:button_click(7))
seven.grid(row=4, column=0, sticky="nsew")
# Number 8
eight = Button(tk_calc, button_params_main, text='8',
             command=lambda:button_click(8))
eight.grid(row=4, column=1, sticky="nsew")
# Number 9
nine = Button(tk_calc, button_params_main, text='9',
             command=lambda:button_click(9))
nine.grid(row=4, column=2, sticky="nsew")
# Division operator
divide = Button(tk_calc, button_params_main, text='/',
             command=lambda:button_click('/'))
divide.grid(row=4, column=3, sticky="nsew")
# Clear all button
clear_all = Button(tk_calc, button_params_main, text='C',
             command=button_clear_all)
clear_all.grid(row=4, column=4, sticky="nsew")

#--5th row--
# Number 4
four = Button(tk_calc, button_params_main, text='4',
             command=lambda:button_click(4))
four.grid(row=5, column=0, sticky="nsew")
# Number 5
five = Button(tk_calc, button_params_main, text='5',
             command=lambda:button_click(5))
five.grid(row=5, column=1, sticky="nsew")
# Number 6
six = Button(tk_calc, button_params_main, text='6',
             command=lambda:button_click(6))
six.grid(row=5, column=2, sticky="nsew")
# Multiplication operator
multiply = Button(tk_calc, button_params_main, text='*',
             command=lambda:button_click('*'))
multiply.grid(row=5, column=3, sticky="nsew")
# Delete one character
delete = Button(tk_calc, button_params_main, text='DEL',
             command=button_delete)
delete.grid(row=5, column=4, sticky="nsew")

#--6th row--
# Number 1
one = Button(tk_calc, button_params_main, text='1',
             command=lambda:button_click(1))
one.grid(row=6, column=0, sticky="nsew")
# Number 2
two = Button(tk_calc, button_params_main, text='2',
             command=lambda:button_click(2))
two.grid(row=6, column=1, sticky="nsew")
# Number 3
three = Button(tk_calc, button_params_main, text='3',
             command=lambda:button_click(3))
three.grid(row=6, column=2, sticky="nsew")
# Minus operator
minus = Button(tk_calc, button_params_main, text='-',
             command=lambda:button_click('-'))
minus.grid(row=6, column=3, sticky="nsew")
# Plus/Minus sign change
sign_change_btn = Button(tk_calc, button_params_main, text='+/-',
             command=sign_change)
sign_change_btn.grid(row=6, column=4, sticky="nsew")

#--7th row--
# Decimal dot
decimal = Button(tk_calc, button_params_main, text='.',
             command=lambda:button_click('.'))
decimal.grid(row=7, column=0, sticky="nsew")
# Number 0
zero = Button(tk_calc, button_params_main, text='0',
             command=lambda:button_click(0))
zero.grid(row=7, column=1, sticky="nsew")
# Percent of a number
percent_btn = Button(tk_calc, button_params_main, text='%',
             command=percent)
percent_btn.grid(row=7, column=2, sticky="nsew")
# Plus operator
plus = Button(tk_calc, button_params_main, text='+',
             command=lambda:button_click('+'))
plus.grid(row=7, column=3, sticky="nsew")
# Equal button
equal = Button(tk_calc, button_params_main, text='=',
             command=button_equal)
equal.grid(row=7, column=4, sticky="nsew")

'''
Mainloop of the window
'''
tk_calc.mainloop()

