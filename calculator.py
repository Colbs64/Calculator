import tkinter as tk

root = tk.Tk()
number = tk.StringVar()
temp_number = ''
current_function = ''

def numbutton_click(x):
    s = number.get()
    s += str(x)
    number.set(s)


def function(choice):
    global temp_number
    global current_function
    current_num = number.get()

    # sets the current function if there is no previously stored numbers
    if temp_number == '':
        temp_number = number.get()
        number.set('')
        current_function = choice

        # else statements reset the function after using a function twice in a row and prints the answer
        # example: 9 * 9 * 9
    else:
        if current_function == 'multiply':
            answer = int(current_num) * int(temp_number)
            number.set(str(answer))
            print('multiplied')

        if current_function == 'divide':
            answer = int(current_num) / int(temp_number)
            number.set(str(answer))
            print('divided')

        if current_function == 'add':
            answer = int(current_num) + int(temp_number)
            number.set(str(answer))
            print('added')

        if current_function == 'subtract':
            answer = int(current_num) - int(temp_number)
            number.set(str(answer))
            print('subtracted')

# print statements so that I know the functions are happening
def output(function, temp_number):
    current_num = number.get()
    if function == 'multiply':
        answer = int(current_num) * int(temp_number)
        number.set(str(answer))
        print('multiplied')

    if function == 'divide':
        # if statement accounts for divisions by zero so that user gets 'undefined' instead of no response
        if current_num or temp_number == 0:
            number.set('undefined')
            print('undefined')

        else:
            answer = int(current_num) / int(temp_number)
            number.set(str(answer))
            print('divided!')

    if function == 'add':
        answer = int(current_num) + int(temp_number)
        number.set(str(answer))
        print('added!')

    if function == 'subtract':
        answer = int(current_num) + int(temp_number)
        number.set(str(answer))
        print('subtracted!')


def clear():
    global temp_number
    global current_function
    number.set('')
    temp_number = ''
    current_function = ''


# keeping window non-resizable. Might add more complex features with resizing later
root.resizable(width=False, height=False)
root.title('Calculator')

number_input = tk.Entry(root, font="Arial, 20", textvariable=number)


# numbers on calc
num0 = tk.Button(root, text=0, command=lambda *args: numbutton_click(0), padx=10, pady=10)
num1 = tk.Button(root, text=1, command=lambda *args: numbutton_click(1), padx=10, pady=10)
num2 = tk.Button(root, text=2, command=lambda *args: numbutton_click(2), padx=10, pady=10)
num3 = tk.Button(root, text=3, command=lambda *args: numbutton_click(3), padx=10, pady=10)
num4 = tk.Button(root, text=4, command=lambda *args: numbutton_click(4), padx=10, pady=10)
num5 = tk.Button(root, text=5, command=lambda *args: numbutton_click(5), padx=10, pady=10)
num6 = tk.Button(root, text=6, command=lambda *args: numbutton_click(6), padx=10, pady=10)
num7 = tk.Button(root, text=7, command=lambda *args: numbutton_click(7), padx=10, pady=10)
num8 = tk.Button(root, text=8, command=lambda *args: numbutton_click(8), padx=10, pady=10)
num9 = tk.Button(root, text=9, command=lambda *args: numbutton_click(9), padx=10, pady=10)
# functions on calc
multiply_button = tk.Button(root, text='*', command=lambda *args: function('multiply'), padx=10, pady=10)
divide_button = tk.Button(root, text='/', command=lambda *args: function('divide'), padx=10, pady=10)
add_button = tk.Button(root, text='+', command=lambda *args: function('add'), padx=10, pady=10)
subtract_button = tk.Button(root, text='-', command=lambda *args: function('subtract'), padx=10, pady=10)

clear_button = tk.Button(root, text='C', command=clear, padx=10, pady=10)


equals = tk.Button(root, text='=', command=lambda *args: output(current_function, temp_number), padx=10, pady=10)


# main box and textbox for numbers
root.grid()
number_input.grid(column=0, row=0, columnspan=5)
num1.grid(column=0, row=1)
num2.grid(column=1, row=1)
num3.grid(column=2, row=1)
num4.grid(column=0, row=2)
num5.grid(column=1, row=2)
num6.grid(column=2, row=2)
num7.grid(column=0, row=3)
num8.grid(column=1, row=3)
num9.grid(column=2, row=3)
num0.grid(column=0, row=4)

clear_button.grid(column=3, row=1)
multiply_button.grid(column=3, row=2)
divide_button.grid(column=3, row=3)
add_button.grid(column=1, row=4)
subtract_button.grid(column=2, row=4)
equals.grid(column=3, row=4)

root.mainloop()
