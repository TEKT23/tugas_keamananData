import tkinter as tk
from tkinter import ttk, messagebox

# Fungsi enkripsi dan dekripsi
def enkripsi(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isupper():
            cipher_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            cipher_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            cipher_text += char
    return cipher_text

def dekripsi(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        if char.isupper():
            plain_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            plain_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            plain_text += char
    return plain_text

def proses_text():
    try:
        shift = int(entry_shift.get())
        input_text = text_input.get("1.0", tk.END).strip()
        if var_mode.get() == "encrypt":
            result = enkripsi(input_text, shift)
        elif var_mode.get() == "decrypt":
            result = dekripsi(input_text, shift)
        else:
            result = "Invalid Mode"
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, result)
    except ValueError:
        messagebox.showerror("Error", "Shift value must be a number!")

root = tk.Tk()
root.title("CIPHER ENCRYPTION MACHINE")
root.geometry("500x400")
root.resizable(False, False)

main_frame = ttk.Frame(root, padding=10)
main_frame.pack(fill="both", expand=True)

ttk.Label(main_frame, text="Set Shift Value").grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_shift = ttk.Entry(main_frame, width=10)
entry_shift.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(main_frame, text="Input Text to Encrypt/Decrypt").grid(row=1, column=0, columnspan=2, sticky="w", padx=5, pady=5)
text_input = tk.Text(main_frame, width=60, height=5)
text_input.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

var_mode = tk.StringVar(value="encrypt")
radio_encrypt = ttk.Radiobutton(main_frame, text="ENCRYPT", variable=var_mode, value="encrypt")
radio_encrypt.grid(row=3, column=0, sticky="w", padx=5, pady=5)
radio_decrypt = ttk.Radiobutton(main_frame, text="DECRYPT", variable=var_mode, value="decrypt")
radio_decrypt.grid(row=3, column=1, sticky="w", padx=5, pady=5)

button_process = ttk.Button(main_frame, text="PROCESS TEXT", command=proses_text)
button_process.grid(row=4, column=0, columnspan=2, pady=10)

ttk.Label(main_frame, text="Output").grid(row=5, column=0, columnspan=2, sticky="w", padx=5, pady=5)
text_output = tk.Text(main_frame, width=60, height=5)
text_output.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
