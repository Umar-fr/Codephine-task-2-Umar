import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_label = ttk.Label(root, text="Password Length:")
        self.length_entry = ttk.Entry(root, width=5)
        self.length_entry.insert(0, "12")  # Default length

        self.use_letters_var = tk.IntVar(value=True)
        self.use_numbers_var = tk.IntVar(value=True)
        self.use_symbols_var = tk.IntVar(value=True)

        self.letters_checkbox = ttk.Checkbutton(root, text="Include Letters", variable=self.use_letters_var)
        self.numbers_checkbox = ttk.Checkbutton(root, text="Include Numbers", variable=self.use_numbers_var)
        self.symbols_checkbox = ttk.Checkbutton(root, text="Include Symbols", variable=self.use_symbols_var)

        self.generate_button = ttk.Button(root, text="Generate Password", command=self.generate_button_click)
        self.copy_button = ttk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.generated_password = None

        # GUI Layout
        self.length_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.length_entry.grid(row=0, column=1, padx=5, pady=5)
        self.letters_checkbox.grid(row=1, column=0, columnspan=2, pady=5, sticky=tk.W)
        self.numbers_checkbox.grid(row=2, column=0, columnspan=2, pady=5, sticky=tk.W)
        self.symbols_checkbox.grid(row=3, column=0, columnspan=2, pady=5, sticky=tk.W)
        self.generate_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.copy_button.grid(row=5, column=0, columnspan=2, pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            use_letters = self.use_letters_var.get()
            use_numbers = self.use_numbers_var.get()
            use_symbols = self.use_symbols_var.get()

            characters = ""
            if use_letters:
                characters += string.ascii_letters
            if use_numbers:
                characters += string.digits
            if use_symbols:
                characters += string.punctuation

            if not characters:
                messagebox.showerror("Error", "Please select at least one character type.")
                return

            # Generate and return the password
            password = ''.join(random.choice(characters) for _ in range(length))
            return password

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for the password length.")

    def generate_button_click(self):
        self.generated_password = self.generate_password()  # Store the generated password
        if self.generated_password:
            messagebox.showinfo("Generated Password", f"Your Password:\n{self.generated_password}")

    def copy_to_clipboard(self):
        if self.generated_password:
            pyperclip.copy(self.generated_password)
            messagebox.showinfo("Clipboard", "Password copied to clipboard!")
        else:
            messagebox.showerror("Error", "Please generate a password first.")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
