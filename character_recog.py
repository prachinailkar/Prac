//pip install opencv-PythonFinalizationError??pip install media pipe
//pip install pillow
//pip install opencv-python
//pip install pytesseract

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import pytesseract

# Set the path to tesseract.exe on your Windows system
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


class OCRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple OCR GUI")

        # Button to load image
        self.btn_load = tk.Button(root, text="Load Image", command=self.load_image)
        self.btn_load.pack(pady=10)

        # Label to display image
        self.image_label = tk.Label(root)
        self.image_label.pack()

        # Text box to show extracted text
        self.text_box = tk.Text(root, height=15, width=60)
        self.text_box.pack(pady=10)

    def load_image(self):
        file_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
        )

        if not file_path:
            return

        # Read image with OpenCV
        image = cv2.imread(file_path)
        if image is None:
            messagebox.showerror("Error", "Failed to load image!")
            return

        # Convert to RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Use pytesseract to extract text
        extracted_text = pytesseract.image_to_string(image_rgb)

        # Display image in Tkinter
        img = Image.fromarray(image_rgb)
        img.thumbnail((400, 400))  # Resize for display
        imgtk = ImageTk.PhotoImage(img)
        self.image_label.config(image=imgtk)
        self.image_label.image = imgtk  # Keep reference

        # Display extracted text
        self.text_box.delete(1.0, tk.END)
        self.text_box.insert(tk.END, extracted_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = OCRApp(root)
    root.mainloop()
