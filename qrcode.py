import tkinter as tk
from tkinter import messagebox
import pyqrcode
import png
from tkinter import filedialog

def generate_qr_code(data, file_path):
    try:
        qr = pyqrcode.create(data)
        qr.png(file_path, scale=8)
        messagebox.showinfo("Success", f"QR Code saved as {file_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def create_gui():
    def on_generate():
        data = data_entry.get()
        if not data:
            messagebox.showerror("Error", "Please enter data for the QR code.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if not file_path:
            return

        generate_qr_code(data, file_path)

    root = tk.Tk()
    root.title("QR Code Generator")

    tk.Label(root, text="Enter URL or String:").grid(row=0, column=0, padx=10, pady=5)
    data_entry = tk.Entry(root, width=50)
    data_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Button(root, text="Generate QR Code", command=on_generate).grid(row=1, columnspan=2, padx=10, pady=10)

    root.mainloop()
if __name__ == "__main__":
    create_gui()

