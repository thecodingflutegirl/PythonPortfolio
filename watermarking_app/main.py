from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import filedialog


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Watermarking App')
        self.geometry("300x300")
        self.columnconfigure(0)
        self.columnconfigure(1)
        self.create_widgets()

    def create_widgets(self):
        self.find_file_btn()
        self.quit_btn()

    def find_file_btn(self):
        self.button = tk.Button(text="Find Picture", command=self.fileDialog)
        self.button.grid(column=0, row=0, pady=20)

    def quit_btn(self):
        self.quit_btn = tk.Button(text='Quit App', command=self.quit)
        self.quit_btn.grid(column=0, row=1, stick=tk.W)

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(
            initialdir="/", title="Select an image", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        self.label = tk.Label(text="Upload Image")
        self.label.grid(sticky=tk.N)
        self.label.configure(text=self.filename)
        self.watermark_image()

    def watermark_image(self):
        image = self.filename
        image = Image.open(image)

        watermarked_image = image.copy()
        draw = ImageDraw.Draw(watermarked_image)
        font = ImageFont.truetype('./Library/Fonts/Arial Unicode.ttf', 15)

        draw.text((0, 0), "WATERMARKED", (255, 255, 255), font=font)

        self.save_image(watermarked_image)

    def save_image(self, image):
        try:
            image.save("./photo_samples/watermarked_img.jpeg")
        except OSError:
            return print("Could not find file path")
        print("Successfully watermarked and saved.")


app = App()
app.mainloop()
