from tkinter import *
from tkinter import messagebox


class Enigma:
    def __init__(self, rotor1_pos, rotor2_pos, rotor3_pos):
        self.rotor1 = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
        self.rotor2 = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
        self.rotor3 = [1, 15, 8, 26, 3, 12, 19, 7, 14, 2, 16, 25, 5, 20, 22, 11, 17, 10, 4, 13, 6, 24, 23, 18, 21, 0]
        self.reflector = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]

        self.rotor1_pos = rotor1_pos
        self.rotor2_pos = rotor2_pos
        self.rotor3_pos = rotor3_pos

    def rotate_rotors(self):
        self.rotor1_pos = (self.rotor1_pos + 1) % 26
        if self.rotor1_pos == 0:
            self.rotor2_pos = (self.rotor2_pos + 1) % 26
            if self.rotor2_pos == 0:
                self.rotor3_pos = (self.rotor3_pos + 1) % 26

    def encrypt_decrypt_char(self, char):
        if not char.isalpha():
            return char

        char = char.upper()
        offset = ord(char) - ord('A')

        # Forward pass through the rotors
        offset = self.rotor1[(offset + self.rotor1_pos) % 26]
        offset = self.rotor2[(offset + self.rotor2_pos) % 26]
        offset = self.rotor3[(offset + self.rotor3_pos) % 26]

        # Reflector
        offset = self.reflector[offset]

        # Backward pass through the rotors
        offset = self.rotor3.index((offset - self.rotor3_pos) % 26)
        offset = self.rotor2.index((offset - self.rotor2_pos) % 26)
        offset = self.rotor1.index((offset - self.rotor1_pos) % 26)

        # Rotate rotors after each character
        self.rotate_rotors()

        return chr(offset + ord('A'))

    def process_text(self, text):
        result = ""
        for char in text:
            result += self.encrypt_decrypt_char(char)
        return result


# GUI Implementation
def process_enigma():
    try:
        text = input_text.get("1.0", END).strip()
        rotor1_pos = int(rotor1_input.get().strip())
        rotor2_pos = int(rotor2_input.get().strip())
        rotor3_pos = int(rotor3_input.get().strip())

        if not (0 <= rotor1_pos < 26 and 0 <= rotor2_pos < 26 and 0 <= rotor3_pos < 26):
            messagebox.showerror("Error", "Posisi rotor harus antara 0 dan 25!")
            return

        enigma = Enigma(rotor1_pos, rotor2_pos, rotor3_pos)
        result = enigma.process_text(text)
        output_text.delete("1.0", END)
        output_text.insert(END, result)

    except ValueError:
        messagebox.showerror("Error", "Input rotor harus angka!")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")


# GUI Setup
root = Tk()
root.title("Enigma Cipher")

Label(root, text="Masukkan Teks").grid(row=0, column=0, padx=10, pady=10, sticky=W)
input_text = Text(root, width=50, height=5)
input_text.grid(row=0, column=1, padx=10, pady=10)

Label(root, text="Posisi Rotor 1").grid(row=1, column=0, padx=10, pady=10, sticky=W)
rotor1_input = Entry(root, width=10)
rotor1_input.grid(row=1, column=1, padx=10, pady=10, sticky=W)

Label(root, text="Posisi Rotor 2").grid(row=2, column=0, padx=10, pady=10, sticky=W)
rotor2_input = Entry(root, width=10)
rotor2_input.grid(row=2, column=1, padx=10, pady=10, sticky=W)

Label(root, text="Posisi Rotor 3").grid(row=3, column=0, padx=10, pady=10, sticky=W)
rotor3_input = Entry(root, width=10)
rotor3_input.grid(row=3, column=1, padx=10, pady=10, sticky=W)

Button(root, text="Proses", command=process_enigma, width=20).grid(row=4, column=1, padx=10, pady=10)

Label(root, text="Hasil").grid(row=5, column=0, padx=10, pady=10, sticky=W)
output_text = Text(root, width=50, height=5)
output_text.grid(row=5, column=1, padx=10, pady=10)

root.mainloop()
