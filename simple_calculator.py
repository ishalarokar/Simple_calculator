import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation")
            return

        messagebox.showinfo("Result", f"The result is: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero.")

# GUI Window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x250")

# Entry fields
tk.Label(window, text="Enter first number:").pack()
entry1 = tk.Entry(window)
entry1.pack()

tk.Label(window, text="Enter second number:").pack()
entry2 = tk.Entry(window)
entry2.pack()

# Operation dropdown
tk.Label(window, text="Select operation:").pack()
operation_var = tk.StringVar(window)
operation_var.set('+')  # default value
tk.OptionMenu(window, operation_var, '+', '-', '*', '/').pack()

# Calculate Button
tk.Button(window, text="Calculate", command=calculate).pack(pady=10)

# Run the app
window.mainloop()