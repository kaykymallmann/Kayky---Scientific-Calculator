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
from asteval import Interpreter  # <-- Importa o asteval para avaliação segura

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

# Function to calculate the factorial of a number with validation
def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Fatorial só é definido para inteiros não negativos.")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fact_func():
    global calc_operator
    try:
        val = float(calc_operator)
        if val != int(val):
            raise ValueError("Use apenas inteiros para fatorial.")
        val = int(val)
        if val < 0:
            raise ValueError("Fatorial de número negativo não existe.")
        result = str(factorial(val))
    except ValueError as e:
        result = f"ERRO: {e}"
    except (TypeError, OverflowError):
        result = "ERRO"
    calc_operator = result
    text_input.set(result)

# Function to calculate trigonometric numbers of an angle in degrees
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
        if abs(tan_val) > 1e10:
            raise ValueError("tan indefinida")
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
            raise ValueError("Raiz de número negativo")
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
        if val >= 0:
            temp = str(val ** (1 / 3))
        else:
            temp = str(-(-val) ** (1 / 3))
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

# Function to evaluate the expression safely using asteval
def button_equal():
    global calc_operator
    aeval = Interpreter()
    try:
        aeval.symtable['sin'] = lambda x: math.sin(math.radians(float(x)))
        aeval.symtable['cos'] = lambda x: math.cos(math.radians(float(x)))
        aeval.symtable['tan'] = lambda x: math.tan(math.radians(float(x)))
        aeval.symtable['log'] = math.log10
        aeval.symtable['ln'] = math.log
        aeval.symtable['sqrt'] = math.sqrt
        aeval.symtable['pi'] = math.pi
        aeval.symtable['e'] = math.e
        aeval.symtable['abs'] = abs
        aeval.symtable['round'] = round
        aeval.symtable['pow'] = pow

        result = aeval(calc_operator)
        if result is None:
            raise ValueError("Expressão inválida")
        calc_operator = str(result)
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
abs_value = Button(tk_calc, button_params, text='abs',
                   command=lambda:button_click('abs('))
abs_value.grid(row=1, column=0, sticky="nsew")
modulo = Button(tk_calc, button_params, text='mod',
                command=lambda:button_click('%'))
modulo.grid(row=1, column=1, sticky="nsew")
int_div = Button(tk_calc, button_params, text='div',
                 command=lambda:button_click('//'))
int_div.grid(row=1, column=2, sticky="nsew")
factorial_button = Button(tk_calc, button_params, text='x!',
                   command=fact_func)
factorial_button.grid(row=1, column=3, sticky="nsew")
eulers_num = Button(tk_calc, button_params, text='e',
                    command=lambda:button_click(str(math.exp(1))))
eulers_num.grid(row=1, column=4, sticky="nsew")

#--2nd row--
sine = Button(tk_calc, button_params, text='sin',
             command=trig_sin)
sine.grid(row=2, column=0, sticky="nsew")
cosine = Button(tk_calc, button_params, text='cos',
             command=trig_cos)
cosine.grid(row=2, column=1, sticky="nsew")
tangent = Button(tk_calc, button_params, text='tan',
             command=trig_tan)
tangent.grid(row=2, column=2, sticky="nsew")
cotangent = Button(tk_calc, button_params, text='cot',
             command=trig_cot)
cotangent.grid(row=2, column=3, sticky="nsew")
pi_num = Button(tk_calc, button_params, text='π',
                command=lambda:button_click(str(math.pi)))
pi_num.grid(row=2, column=4, sticky="nsew")

#--3rd row--
second_power = Button(tk_calc, button_params, text='x\u00B2',
             command=lambda:button_click('**2'))
second_power.grid(row=3, column=0, sticky="nsew")
third_power = Button(tk_calc, button_params, text='x\u00B3',
             command=lambda:button_click('**3'))
third_power.grid(row=3, column=1, sticky="nsew")
square_rt = Button(tk_calc, button_params, text='\u221A',
             command=square_root)
square_rt.grid(row=3, column=2, sticky="nsew")
third_rt = Button(tk_calc, button_params, text='\u221B',
             command=third_root)
third_rt.grid(row=3, column=3, sticky="nsew")
exponent = Button(tk_calc, button_params, text='exp',
             command=exp_func)
exponent.grid(row=3, column=4, sticky="nsew")

#--4th row--
seven = Button(tk_calc, button_params_main, text='7',
               command=lambda:button_click(7))
seven.grid(row=4, column=0, sticky="nsew")
eight = Button(tk_calc, button_params_main, text='8',
               command=lambda:button_click(8))
eight.grid(row=4, column=1, sticky="nsew")
nine = Button(tk_calc, button_params_main, text='9',
               command=lambda:button_click(9))
nine.grid(row=4, column=2, sticky="nsew")
divide = Button(tk_calc, button_params_main, text='/',
                command=lambda:button_click('/'))
divide.grid(row=4, column=3, sticky="nsew")
clear_all = Button(tk_calc, button_params_main, text='C',
                   command=button_clear_all)
clear_all.grid(row=4, column=4, sticky="nsew")

#--5th row--
four = Button(tk_calc, button_params_main, text='4',
              command=lambda:button_click(4))
four.grid(row=5, column=0, sticky="nsew")
five = Button(tk_calc, button_params_main, text='5',
              command=lambda:button_click(5))
five.grid(row=5, column=1, sticky="nsew")
six = Button(tk_calc, button_params_main, text='6',
              command=lambda:button_click(6))
six.grid(row=5, column=2, sticky="nsew")
multiply = Button(tk_calc, button_params_main, text='*',
                  command=lambda:button_click('*'))
multiply.grid(row=5, column=3, sticky="nsew")
delete = Button(tk_calc, button_params_main, text='DEL',
                command=button_delete)
delete.grid(row=5, column=4, sticky="nsew")

#--6th row--
one = Button(tk_calc, button_params_main, text='1',
             command=lambda:button_click(1))
one.grid(row=6, column=0, sticky="nsew")
two = Button(tk_calc, button_params_main, text='2',
             command=lambda:button_click(2))
two.grid(row=6, column=1, sticky="nsew")
three = Button(tk_calc, button_params_main, text='3',
               command=lambda:button_click(3))
three.grid(row=6, column=2, sticky="nsew")
minus = Button(tk_calc, button_params_main, text='-',
               command=lambda:button_click('-'))
minus.grid(row=6, column=3, sticky="nsew")
sign = Button(tk_calc, button_params_main, text='+/-',
              command=sign_change)
sign.grid(row=6, column=4, sticky="nsew")

#--7th row--
zero = Button(tk_calc, button_params_main, text='0',
              command=lambda:button_click(0))
zero.grid(row=7, column=0, sticky="nsew")
dot = Button(tk_calc, button_params_main, text='.',
             command=lambda:button_click('.'))
dot.grid(row=7, column=1, sticky="nsew")
percent_button = Button(tk_calc, button_params_main, text='%',
                        command=percent)
percent_button.grid(row=7, column=2, sticky="nsew")
plus = Button(tk_calc, button_params_main, text='+',
              command=lambda:button_click('+'))
plus.grid(row=7, column=3, sticky="nsew")
equal = Button(tk_calc, button_params_main, text='=',
               command=button_equal)
equal.grid(row=7, column=4, sticky="nsew")

tk_calc.mainloop()
