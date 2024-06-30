import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, min_uppercase, min_lowercase, min_digits, min_symbols, include_special_chars):
    if length < (min_uppercase + min_lowercase + min_digits + min_symbols):
        return "Error: Minimum length requirement not met."

    password_characters = []
    
    # Add required number of each type of character
    password_characters.extend(random.choices(string.ascii_uppercase, k=min_uppercase))
    password_characters.extend(random.choices(string.ascii_lowercase, k=min_lowercase))
    password_characters.extend(random.choices(string.digits, k=min_digits))
    
    if include_special_chars:
        symbols = string.punctuation
        password_characters.extend(random.choices(symbols, k=min_symbols))
    
    # If the password still needs more characters, fill the rest with random characters
    if len(password_characters) < length:
        all_chars = string.ascii_letters + string.digits
        if include_special_chars:
            all_chars += string.punctuation
        password_characters.extend(random.choices(all_chars, k=length - len(password_characters)))
    
    # Shuffle the password characters to ensure randomness
    random.shuffle(password_characters)
    
    return ''.join(password_characters)

def create_gui():
    def on_generate():
        try:
            length = int(length_entry.get())
            min_uppercase = int(min_uppercase_entry.get())
            min_lowercase = int(min_lowercase_entry.get())
            min_digits = int(min_digits_entry.get())
            min_symbols = int(min_symbols_entry.get())
            include_special_chars = special_chars_var.get()
            
            password = generate_password(
                length, min_uppercase, min_lowercase, min_digits, min_symbols, include_special_chars
            )
            
            if "Error" in password:
                messagebox.showerror("Error", password)
            else:
                result_label.config(text=f"Generated Password: {password}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

    root = tk.Tk()
    root.title("Password Generator")
    
    # Labels and entries for user inputs
    tk.Label(root, text="Length:").grid(row=0, column=0, padx=10, pady=5)
    length_entry = tk.Entry(root)
    length_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Min Uppercase:").grid(row=1, column=0, padx=10, pady=5)
    min_uppercase_entry = tk.Entry(root)
    min_uppercase_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Min Lowercase:").grid(row=2, column=0, padx=10, pady=5)
    min_lowercase_entry = tk.Entry(root)
    min_lowercase_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(root, text="Min Digits:").grid(row=3, column=0, padx=10, pady=5)
    min_digits_entry = tk.Entry(root)
    min_digits_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(root, text="Min Symbols:").grid(row=4, column=0, padx=10, pady=5)
    min_symbols_entry = tk.Entry(root)
    min_symbols_entry.grid(row=4, column=1, padx=10, pady=5)

    special_chars_var = tk.BooleanVar()
    tk.Checkbutton(root, text="Include Special Characters", variable=special_chars_var).grid(row=5, columnspan=2, padx=10, pady=5)

    tk.Button(root, text="Generate Password", command=on_generate).grid(row=6, columnspan=2, padx=10, pady=10)
    
    result_label = tk.Label(root, text="")
    result_label.grid(row=7, columnspan=2, padx=10, pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    create_gui()
