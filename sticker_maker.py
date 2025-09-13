# sticker_maker.pyw
# A simple app to make stickers by removing backgrounds

import tkinter as tk
from tkinter import filedialog, messagebox
from rembg import remove
from PIL import Image

def make_sticker():
    try:
        # Ask user to pick an image
        input_path = filedialog.askopenfilename(
            title="Select an image",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.webp")]
        )
        if not input_path:
            return  # User cancelled

        # Output file name
        output_path = input_path.rsplit(".", 1)[0] + "_sticker.png"

        # Open and remove background
        input_image = Image.open(input_path)
        output_image = remove(input_image)

        # Save result
        output_image.save(output_path, "PNG")

        messagebox.showinfo("Success", f"Sticker saved as:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# GUI setup
root = tk.Tk()
root.title("Sticker Maker")

label = tk.Label(root, text="Click below to select an image and make a sticker!", pady=10)
label.pack()

button = tk.Button(root, text="Choose Image", command=make_sticker, width=20, height=2)
button.pack(pady=20)

root.mainloop()
