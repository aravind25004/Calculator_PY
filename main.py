import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(False, False)

        self.show_instructions()

    def show_instructions(self):
        instruction_frame = tk.Frame(self.root, padx=20, pady=20, bg='#3498DB')
        instruction_frame.pack()

        instruction_label = tk.Label(instruction_frame, text="Welcome to the Calculator!\n\n"
                                                             "1. Enter numbers and operators using buttons.\n"
                                                             "2. Press '=' to calculate the result.\n"
                                                             "3. Press 'C' to clear the input field.", bg='#3498DB', fg='#FFFFFF')
        instruction_label.pack()

        next_button = tk.Button(instruction_frame, text="Next", command=self.show_calculator, bg='#E74C3C', fg='#FFFFFF')
        next_button.pack(pady=10)

    def show_calculator(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        calculator_frame = tk.Frame(self.root, padx=20, pady=20, bg='#ECF0F1')
        calculator_frame.pack()

        self.entry_var = tk.StringVar()
        entry_field = tk.Entry(calculator_frame, textvariable=self.entry_var, font=('Arial', 18), bd=10, insertwidth=4, width=14, justify='right', bg='#F2F3F4')
        entry_field.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            if text == '+':
                button = tk.Button(calculator_frame, text=text, padx=18, pady=20, font=('Arial', 18), command=lambda t=text: self.on_button_click(t))
            else:
                button = tk.Button(calculator_frame, text=text, padx=20, pady=20, font=('Arial', 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)

    def on_button_click(self, value):
        if value == 'C':
            self.entry_var.set('')
        elif value == '=':
            try:
                result = eval(self.entry_var.get())
                self.entry_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Expression: {e}")
        else:
            current_text = self.entry_var.get()
            self.entry_var.set(current_text + value)


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
