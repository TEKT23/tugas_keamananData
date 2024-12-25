from tkinter import *
from tkinter import messagebox
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64

# Fungsi untuk mengenkripsi
def encrypt_text():
    try:
        plain_text = text_input.get("1.0", END).strip()
        key = key_input.get().strip()

        if len(key) != 8:
            messagebox.showerror("Error", "Kunci harus 8 karakter!")
            return

        des = DES.new(key.encode('utf-8'), DES.MODE_ECB)
        padded_text = pad(plain_text.encode('utf-8'), DES.block_size)
        encrypted_text = des.encrypt(padded_text)
        encoded_text = base64.b64encode(encrypted_text).decode('utf-8')

        text_output.delete("1.0", END)
        text_output.insert(END, encoded_text)
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# Fungsi untuk mendekripsi
def decrypt_text():
    try:
        encrypted_text = text_input.get("1.0", END).strip()
        key = key_input.get().strip()

        if len(key) != 8:
            messagebox.showerror("Error", "Kunci harus 8 karakter!")
            return

        des = DES.new(key.encode('utf-8'), DES.MODE_ECB)
        decoded_text = base64.b64decode(encrypted_text)
        decrypted_text = unpad(des.decrypt(decoded_text), DES.block_size).decode('utf-8')

        text_output.delete("1.0", END)
        text_output.insert(END, decrypted_text)
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# Membuat GUI
root = Tk()
root.title("DES Encryption/Decryption")
        
Label(root, text="Teks Masukan").grid(row=0, column=0, padx=10, pady=10, sticky=W)
text_input = Text(root, width=50, height=5)
text_input.grid(row=0, column=1, padx=10, pady=10)

Label(root, text="Kunci (8 karakter)").grid(row=1, column=0, padx=10, pady=10, sticky=W)
key_input = Entry(root, width=50)
key_input.grid(row=1, column=1, padx=10, pady=10)

encrypt_button = Button(root, text="Enkripsi", command=encrypt_text, width=20)
encrypt_button.grid(row=2, column=0, padx=10, pady=10)

decrypt_button = Button(root, text="Dekripsi", command=decrypt_text, width=20)
decrypt_button.grid(row=2, column=1, padx=10, pady=10)

Label(root, text="Hasil").grid(row=3, column=0, padx=10, pady=10, sticky=W)
text_output = Text(root, width=50, height=5)
text_output.grid(row=3, column=1, padx=10, pady=10)

root.mainloop()
