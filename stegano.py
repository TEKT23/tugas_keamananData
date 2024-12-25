import os
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox, ttk, StringVar
from stegano import lsb


class SteganographyApp:
    def __init__(self, master):
        self.master = master
        master.title("Steganography Application")
        master.geometry("500x400")
        master.resizable(False, False)

        # Main Title
        title_label = Label(master, text="Steganography GUI", font=("Arial", 16, "bold"), pady=10)
        title_label.pack()

        # Tab Control
        tab_control = ttk.Notebook(master)

        # Hide Tab
        hide_tab = ttk.Frame(tab_control)
        tab_control.add(hide_tab, text="Hide Message")

        # Reveal Tab
        reveal_tab = ttk.Frame(tab_control)
        tab_control.add(reveal_tab, text="Reveal Message")

        tab_control.pack(expand=1, fill="both")

        # === Hide Message Tab ===
        self.image_path = StringVar()

        ttk.Label(hide_tab, text="Select Image:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.image_entry = ttk.Entry(hide_tab, textvariable=self.image_path, width=50, state="readonly")
        self.image_entry.grid(row=0, column=1, padx=10)
        ttk.Button(hide_tab, text="Browse", command=self.select_image).grid(row=0, column=2, padx=5)

        ttk.Label(hide_tab, text="Enter Message:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.message_entry = ttk.Entry(hide_tab, width=60)
        self.message_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

        ttk.Label(hide_tab, text="Save Image As:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.save_entry = ttk.Entry(hide_tab, width=60)
        self.save_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

        ttk.Button(hide_tab, text="Hide Message", command=self.hide_message).grid(row=3, column=0, columnspan=3, pady=20)

        # === Reveal Message Tab ===
        ttk.Label(reveal_tab, text="Select Image:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.reveal_image_path = StringVar()
        self.reveal_image_entry = ttk.Entry(reveal_tab, textvariable=self.reveal_image_path, width=50, state="readonly")
        self.reveal_image_entry.grid(row=0, column=1, padx=10)
        ttk.Button(reveal_tab, text="Browse", command=self.select_reveal_image).grid(row=0, column=2, padx=5)

        ttk.Button(reveal_tab, text="Reveal Message", command=self.reveal_message).grid(row=1, column=0, columnspan=3, pady=20)

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg")])
        if file_path:
            self.image_path.set(file_path)
        else:
            messagebox.showerror("Error", "No image selected!")

    def select_reveal_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg")])
        if file_path:
            self.reveal_image_path.set(file_path)
        else:
            messagebox.showerror("Error", "No image selected!")

    def hide_message(self):
        image_path = self.image_path.get()
        message = self.message_entry.get()
        save_path = self.save_entry.get()

        if not image_path:
            messagebox.showerror("Error", "Please select an image!")
            return
        if not message:
            messagebox.showerror("Error", "Please enter a message to hide!")
            return
        if not save_path:
            messagebox.showerror("Error", "Please specify a save file path!")
            return

        try:
            secret = lsb.hide(image_path, message)
            secret.save(save_path)
            messagebox.showinfo("Success", "Message hidden successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to hide message: {e}")

    def reveal_message(self):
        image_path = self.reveal_image_path.get()
        if not image_path:
            messagebox.showerror("Error", "Please select an image!")
            return

        try:
            message = lsb.reveal(image_path)
            if message:
                messagebox.showinfo("Hidden Message", f"Message: {message}")
            else:
                messagebox.showinfo("No Message", "No hidden message found.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to reveal message: {e}")


if __name__ == "__main__":
    root = Tk()
    app = SteganographyApp(root)
    root.mainloop()
