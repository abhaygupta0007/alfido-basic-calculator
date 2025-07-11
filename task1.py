import tkinter as tk
from tkinter import ttk

class SmartCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Smart Calculator")
        self.geometry("350x500")
        self.resizable(False, False)
        self.configure(bg="#2b2b2b")

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()
        self.bind_keys()

    def create_widgets(self):
        # Display field
        entry_frame = tk.Frame(self, bg="#2b2b2b")
        entry_frame.pack(expand=True, fill="both")

        input_field = tk.Entry(
            entry_frame,
            font=("Helvetica", 24),
            textvariable=self.input_text,
            justify="right",
            bd=0,
            bg="#1e1e1e",
            fg="#ffffff",
            insertbackground="white"
        )
        input_field.pack(pady=20, padx=10, ipady=10, fill="x")

        # Buttons
        btns_frame = tk.Frame(self, bg="#2b2b2b")
        btns_frame.pack()

        buttons = [
            ("C", "←", "%", "/"),
            ("7", "8", "9", "*"),
            ("4", "5", "6", "-"),
            ("1", "2", "3", "+"),
            ("0", ".", "=", ""),
        ]

        for row in buttons:
            row_frame = tk.Frame(btns_frame, bg="#2b2b2b")
            row_frame.pack(expand=True, fill="both")
            for btn_text in row:
                if btn_text:
                    btn = tk.Button(
                        row_frame,
                        text=btn_text,
                        font=("Helvetica", 18),
                        fg="white",
                        bg="#3a3a3a",
                        activebackground="#505050",
                        activeforeground="white",
                        bd=0,
                        relief=tk.FLAT,
                        command=lambda x=btn_text: self.on_button_click(x)
                    )
                    btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)

    def bind_keys(self):
        self.bind("<Key>", self.on_keypress)

    def on_keypress(self, event):
        char = event.char
        if char in "0123456789.+-*/%":
            self.expression += char
        elif event.keysym == "Return":
            self.evaluate()
        elif event.keysym == "BackSpace":
            self.expression = self.expression[:-1]
        elif event.keysym == "Escape":
            self.expression = ""
        self.input_text.set(self.expression)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "←":
            self.expression = self.expression[:-1]
        elif char == "=":
            self.evaluate()
            return
        else:
            self.expression += str(char)
        self.input_text.set(self.expression)

    def evaluate(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except:
            self.input_text.set("Error")
            self.expression = ""

if __name__ == "__main__":
    app = SmartCalculator()
    app.mainloop()
